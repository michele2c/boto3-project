import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    # iterate over values stored in response and store values of 'Reservations' key
    # in reservation
    for instance in reservation['Instances']:
         # iterate over values stored in reservation and store values of 'Instances' key
         # in instance
        print(instance['InstanceId'], instance['State']['Name'])