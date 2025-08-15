import json
import boto3
from botocore.exceptions import ClientError

# Create AWS SES client
ses_client = boto3.client('ses', region_name="us-east-1")  

def send_email(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        receiver_email = body.get("receiver_email")
        subject = body.get("subject")
        body_text = body.get("body_text")

        # Validation
        if not receiver_email or not subject or not body_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "receiver_email, subject, and body_text are required."})
            }

        # Sending email using AWS SES
        try:
            response = ses_client.send_email(
                Source="your_verified_email@example.com",  
                Destination={
                    "ToAddresses": [receiver_email]
                },
                Message={
                    "Subject": {"Data": subject},
                    "Body": {
                        "Text": {"Data": body_text}
                    }
                }
            )
        except ClientError as e:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": e.response['Error']['Message']})
            }

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Email sent successfully",
                "message_id": response["MessageId"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
