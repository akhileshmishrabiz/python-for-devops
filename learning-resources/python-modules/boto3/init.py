# python -m venv pythonondevops
# source pythonondevops/bin/activate
# pip install boto3

# aws configure

# F string

name = "akhilesh"
role = "devops"
age = 34
exp = 12

print(f' Name: {name} \n Role: {role} \n Age: {age}\n WorkExperience: {exp} ')


######### exp 1: 1 instance ##########
import boto3

client = boto3.client('ec2', region_name='ap-south-1')

response = client.describe_instances(
    InstanceIds=[
        'i-04da5a5a33a1a9bb2',
    ],
)

image = response["Reservations"][0]["Instances"][0]["ImageId"]
pub_ip = response["Reservations"][0]["Instances"][0]["NetworkInterfaces"][0]["Association"]["PublicIp"]


print(image, pub_ip)


########## exp 2: using filter to get running instances #####

import boto3

client = boto3.client('ec2', region_name='ap-south-1')

response = client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ],
)

out = response['Reservations']

for i in out:
    instance_id  = i["Instances"][0]["InstanceId"]
    mac  = i["Instances"][0]["NetworkInterfaces"][0]["MacAddress"]
    pub_ip = i["Instances"][0]["NetworkInterfaces"][0]["Association"]["PublicIp"]


    print(f" InstanceID:{instance_id} \n MacADDR:{mac} \nPubIP: {pub_ip}")



