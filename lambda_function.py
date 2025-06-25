import boto3
import json
from datetime import datetime, timedelta

REGION = "us-west-2"
ALB_FULL_NAME = "app/Swetabh-AutoScaler-ALB-1/c4d747aee66e5d46"
SNS_TOPIC_ARN = "arn:aws:sns:us-west-2:975050024946:Swetabh-EC2AutoScalerTopic:5ae2f211-58d0-4db5-8915-7083f219e661"
AMI_ID = "ami-05f991c49d264708f"
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "swetabh-key"
SECURITY_GROUP_IDS = ["sg-00df7d71e32979524"]
SUBNET_ID = "subnet-06bd72b2e4cb41d10"

ec2 = boto3.client("ec2", region_name=REGION)
cloudwatch = boto3.client("cloudwatch", region_name=REGION)
sns = boto3.client("sns", region_name=REGION)

def lambda_handler(event, context):
    end = datetime.utcnow()
    start = end - timedelta(minutes=5)

    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/ApplicationELB",
        MetricName="NetworkIn",
        Dimensions=[
            {"Name": "LoadBalancer", "Value": ALB_FULL_NAME}
        ],
        StartTime=start,
        EndTime=end,
        Period=300,
        Statistics=["Average"]
    )

    datapoints = response["Datapoints"]
    avg_load = datapoints[0]["Average"] if datapoints else 0
    print(f"Average Load (NetworkIn): {avg_load:.2f} bytes")

    # Fetch all EC2 instances launched by this scaler
    instances = ec2.describe_instances(
        Filters=[{"Name": "tag:AutoScaler", "Values": ["true"]}]
    )

    instance_ids = [
        inst["InstanceId"]
        for res in instances["Reservations"]
        for inst in res["Instances"]
    ]

    message = ""

    if avg_load > 80000000:  # >80MB in 5 minutes
        print("High load detected. Launching new EC2 instance...")
        ec2.run_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            MaxCount=1,
            MinCount=1,
            NetworkInterfaces=[{
                "SubnetId": SUBNET_ID,
                "DeviceIndex": 0,
                "AssociatePublicIpAddress": True,
                "Groups": SECURITY_GROUP_IDS
            }],
            TagSpecifications=[{
                "ResourceType": "instance",
                "Tags": [
                    {"Key": "AutoScaler", "Value": "true"},
                    {"Key": "CreatedBy", "Value": "LambdaAutoScaler"}
                ]
            }]
        )
        message = f"🚀 High load ({avg_load:.2f}) - Launched a new EC2 instance."

    elif avg_load < 20000000 and len(instance_ids) > 1:  # <20MB and more than 1 instance
        print("Low load detected. Terminating an EC2 instance...")
        instance_to_terminate = instance_ids[-1]
        ec2.terminate_instances(InstanceIds=[instance_to_terminate])
        message = f"🧹 Low load ({avg_load:.2f}) - Terminated instance {instance_to_terminate}."

    else:
        message = f"📊 Load normal ({avg_load:.2f}) - No scaling action."

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="EC2 AutoScaler Update",
        Message=message
    )

    return {
        "statusCode": 200,
        "message": message
    }
