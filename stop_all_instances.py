import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

#Get all running instances
response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for reservation in response['Reservations']:
    # iterate over values stored in response and store values of 'Reservations' key
    # in reservation
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
         # iterate over values stored in reservation and store values of 'Instances' key
         # in instance
        print(f"Stopping instance: {instance_id}")
        ec2.stop_instances(InstanceIds=[instance_id])
            