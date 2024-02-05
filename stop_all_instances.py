import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get all running instances
response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
# Stop instances
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f'Stopping instance: {instance_id}')
