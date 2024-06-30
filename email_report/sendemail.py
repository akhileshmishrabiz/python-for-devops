import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ses_client = boto3.client('ses')

FROM = "aditiyamishranit@gmail.com"
TO = ['livingdevops@gmail.com', 'akhileshmishra121990@gmail.com']

subject = "this is the subject of email from python - html"
body_text = """
<html>
<body style="font-family: Arial, sans-serif; color: #333;">
    <table width="100%" cellpadding="0" cellspacing="0" style="max-width: 600px; margin: 0 auto; border: 1px solid #ddd; padding: 20px;">
        <tr>
            <td>
                <h1 style="color: #4CAF50;">Join Our DevOps Mentorship Program</h1>
                <p>Dear Developer,</p>
                <p>Are you looking to enhance your skills in DevOps and advance your career? Our personalized DevOps mentorship program is designed to guide you through the complexities of modern software development practices.</p>
                <h2 style="color: #4CAF50;">What We Offer</h2>
                <ul>
                    <li>One-on-one mentoring sessions</li>
                    <li>Hands-on experience with CI/CD pipelines</li>
                    <li>Insights into cloud infrastructure management</li>
                    <li>Best practices for automation and monitoring</li>
                </ul>
                <p>Whether you're just starting out or looking to refine your skills, our mentorship program will provide you with the knowledge and support you need to succeed.</p>
                <p style="text-align: center;">
                    <a href="https://livingdevops.com" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Learn More</a>
                </p>
                <p>Best regards,<br>Your Name<br>DevOps Mentor</p>
            </td>
        </tr>
    </table>
</body>
</html>


"""

msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = FROM
msg["To"] = ", ".join(TO)
# body_part = MIMEText(body, "plain")
part1 = MIMEText(body_text, 'plain')
part2 = MIMEText(body_text, 'html')
msg.attach(part2)

response = ses_client.send_raw_email(
    Source=msg["From"],
    Destinations=TO,
    RawMessage={"Data": msg.as_string()},
)

print(response)
