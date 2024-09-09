import boto3

ssm = boto3.client('ssm')
autoscaling = boto3.client('autoscaling')

def get_instance_ids_from_asg(asg_name: str) -> list:
    """
    Retrieves a list of EC2 instance IDs that are part of the specified Auto Scaling group.
    
    :param asg_name: Name of the Auto Scaling group
    :return: List of instance IDs in the Auto Scaling group
    """
    # Create an Auto Scaling client
    autoscaling = boto3.client('autoscaling')
    
    # Get the details of the specified Auto Scaling group
    response = autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    
    # Extract instance IDs from the response
    instance_ids = [
        instance['InstanceId'] 
        for instance in response['AutoScalingGroups'][0]['Instances'] 
        if instance['LifecycleState'] == 'InService'
    ]
    
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
asg_name = "cluster-training"
instance_ids = get_instance_ids_from_asg(asg_name)

association_id = "fd668724-35c7-4313-bd65-eeac529a1923"
send_ssm_command(instance_ids, association_id )

