import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv   

# Load .env variables
load_dotenv()

# Gmail SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

def send_email(event, context):
    try:
        # Parse request body
        body = json.loads(event.get("body", "{}"))

        receiver_email = body.get("receiver_email")
        subject = body.get("subject")
        body_text = body.get("body_text")

        # Validate input
        if not receiver_email or not subject or not body_text:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "receiver_email, subject, and body_text are required."
                })
            }

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body_text, "plain"))

        # Connect to Gmail SMTP and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())

        # Success response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Email sent successfully to {receiver_email}",
                "subject": subject,
                "body_text": body_text
            })
        }

    except Exception as e:
        # Error response
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
