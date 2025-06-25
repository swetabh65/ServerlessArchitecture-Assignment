import boto3
import datetime

def lambda_handler(event, context):
    print("Event received:", event)
    
    try:
        instance_id = event['detail']['instance-id']
        ec2 = boto3.client('ec2')
        launch_date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
        
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': 'LaunchDate', 'Value': launch_date},
                {'Key': 'Owner', 'Value': 'SwetabhSonal'}
            ]
        )
        
        print(f"✅ Instance {instance_id} tagged successfully.")
        
    except Exception as e:
        print(f"❌ Error tagging instance: {str(e)}")
