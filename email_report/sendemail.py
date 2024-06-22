from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import boto3


ses= boto3.client('ses')

TO_EMAILS = ["to_email_address"]
FROM_EMAIL = "FROM_EMAIL_ADDRESS"

def send_email(subject, body, to_emails):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = FROM_EMAIL
    msg["To"] = ", ".join(to_emails)
    body_part = MIMEText(body, "plain")
    msg.attach(body_part)

    response = ses.send_raw_email(
        Source=msg["From"],
        Destinations=to_emails,
        RawMessage={"Data": msg.as_string()},
    )
    print(f"Email sent via AWS SES! Message ID: {response['MessageId']}")
