import  boto3
sqs = boto3.client('sqs')
def list_queue_urls():
    return sqs.list_queues(
    )['QueueUrls']


def get_kms_key(queue_url):
    try:
        response = sqs.get_queue_attributes(
            QueueUrl= queue_url,
            AttributeNames=[
                'KmsMasterKeyId']
        )
        return response['Attributes']['KmsMasterKeyId']
    except Exception as e:
        # print(f"some error happend \n{e}")
        return None
def queue_without_encryption():
    queue_without_encryption = []
    for queue_url in list_queue_urls():
        kms = get_kms_key(queue_url)
        if not kms:
            queue_without_encryption.append(queue_url)
    return queue_without_encryption

def encrypt_queue(queue_url, kms_key):
    response = sqs.set_queue_attributes(
        QueueUrl=queue_url,
        Attributes={
            'KmsMasterKeyId': kms_key
        }
    )
    return response


def run(kms_key):
    for item in queue_without_encryption():
        encrypt_queue(item, kms_key)
