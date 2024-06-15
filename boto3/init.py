# python -m venv pythonondevops
# source pythonondevops/bin/activate
# pip install boto3

# aws configure


import boto3

client = boto3.client('ec2', region_name='ap-south-1')

response = client.describe_instances(
    InstanceIds=[
        'i-04da5a5a33a1a9bb2',
    ],
)

print(response)
