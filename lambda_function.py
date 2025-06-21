import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name='us-west-2')  # Oregon region

    # Auto-Stop instances
    stop_instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Stop']}]
    )
    stop_ids = [instance.id for instance in stop_instances if instance.state['Name'] == 'running']
    if stop_ids:
        ec2.instances.filter(InstanceIds=stop_ids).stop()
        print(f'Stopped instances: {stop_ids}')
    else:
        print('No running instances to stop.')

    # Auto-Start instances
    start_instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Start']}]
    )
    start_ids = [instance.id for instance in start_instances if instance.state['Name'] == 'stopped']
    if start_ids:
        ec2.instances.filter(InstanceIds=start_ids).start()
        print(f'Started instances: {start_ids}')
    else:
        print('No stopped instances to start.')

    return {
        'statusCode': 200,
        'body': 'EC2 instances managed successfully.'
    }
