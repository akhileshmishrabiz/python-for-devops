## https://cloud.google.com/pubsub/docs/samples/pubsub-create-topic?hl=en
# pip install google-cloud-storage
# pip install google-cloud-pubsub
# pip install google-cloud

from google.cloud import storage
from google.oauth2 import service_account
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
service_account_key_path = "path_to_service_account_key_json"
# Authenticate with Google Cloud using the service account key
credentials = service_account.Credentials.from_service_account_file(service_account_key_path)
project_id = "gcp-project-id"
topic_id = "topic-name"
# Create a client
publisher = pubsub_v1.PublisherClient(credentials=credentials)
topic_path = publisher.topic_path(project_id, topic_id)

def sample_list_topic_subscriptions():
    response = publisher.list_topic_subscriptions(request={"topic": topic_path})
    for subscription in response:
        print(subscription)

def list_pubsub_topics(project_id):
    """Lists all the Pub/Sub topics and subscriptions in a project."""
    # List all the topics in the project
    topics = publisher.list_topics(project=f"projects/{project_id}")

    print("Pub/Sub topics:")
    for topic in topics:
        print(topic.name)

def create_bucket_notifications(bucket_name, topic_name):
    """Creates a notification configuration for a bucket."""
    # Make sure the service account have permission to publish to pubsub
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    notification = bucket.notification(topic_name=topic_name)
    notification.create()

    print(f"Successfully created notification with ID {notification.notification_id} for bucket {bucket_name}")

def publish_to_topic():
    for n in range(1, 10):
        data_str = f"Message number {n}"
        # Data must be a bytestring
        data = data_str.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data)
        print(future.result())

    print(f"Published messages to {topic_path}.")

def subscribe_to_topic():
    subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    # Number of seconds the subscriber should listen for messages
    timeout = 5.0

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        print(f"Received {message}.")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")

    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception is encountered first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.
