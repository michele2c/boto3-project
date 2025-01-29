# AWS EC2 Auto Stop Script

## Description

This Python script uses the AWS SDK (`boto3`) to stop all running EC2 instances with a tag. It retrieves the instances matching this criteria and stops them to save costs when not in use.

### Prerequisites

Before running this script, ensure you have the following:

- AWS CLI configured with appropriate credentials (`aws configure`).

- Python installed (>=3.6).

- `boto3` library installed (pip install boto3).

### Installation

1. Clone or download this repository.

2. Install dependencies:

pip install boto3

### Usage

Run the script with: ```python script.py```

### How It Works

1. Connects to AWS EC2 using boto3.

2. Retrieves all running EC2 instances tagged. (This example instances are tagged as Environment:Dev).

3. Stops each matching instance and prints a confirmation message.

### Code
```python
import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get all running instances and tagged as Environment:Dev
response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']},
            {'Name': 'tag:Environment', 'Values': ['Dev']}]
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']

        ec2.stop_instances(InstanceIds=[instance_id])
        print(f'Stopping instance: {instance_id} on Environment:Dev tag')
```

> [!NOTE]
> Ensure that the IAM role or user executing this script has the necessary permissions (`ec2:DescribeInstances` and `ec2:StopInstances`).
