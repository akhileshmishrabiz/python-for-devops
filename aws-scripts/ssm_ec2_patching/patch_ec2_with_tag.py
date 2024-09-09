import boto3

# Create EC2 and SSM resources
ec2 = boto3.resource('ec2')
ssm = boto3.client('ssm')

instance_tag_key = "Name"
instance_tag_value = "cluster-training"
association_id = "fd668724-35c7-4313-bd65-eeac529a8ea6"

def run_baseline_on_ec2instances(tag_key: str, tag_value: str) -> list:
    """
    This function returns a list of EC2 instance IDs that have the specified tag key and value and are running.
    
    :param tag_key: The tag key to filter instances by
    :param tag_value: The tag value to filter instances by
    :return: List of instance IDs that match the tag
    """
    # Filter instances by tag and running state
    instances = ec2.instances.filter(
        Filters=[
            {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )
    
    # Create a list to store matching instance IDs
    instance_ids = [instance.id for instance in instances]
    
    return instance_ids

def send_ssm_command(instance_ids: list, association_id: str):
    """
    Sends the AWS-RunPatchBaseline SSM command to the provided instance IDs.
    
    :param instance_ids: List of EC2 instance IDs to send the command to
    """
    if not instance_ids:
        print("No running instances found to patch.")
        return

    response = ssm.send_command(
        DocumentName="AWS-RunPatchBaseline",
        DocumentVersion="1",
        Targets=[{'Key': 'InstanceIds', 'Values': instance_ids}],
        Parameters={
            "AssociationId": [association_id],
            "Operation": ["Install"],
            "RebootOption": ["RebootIfNeeded"],
            "SnapshotId": [""]
        },
        TimeoutSeconds=600,
        MaxConcurrency="50",
        MaxErrors="0",
    )
    
    print(f"Command sent. Command ID: {response['Command']['CommandId']}")

# Example usage
instance_ids = run_baseline_on_ec2instances(instance_tag_key, instance_tag_value)
send_ssm_command(instance_ids)
