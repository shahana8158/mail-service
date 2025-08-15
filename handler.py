import json
# import boto3
# from botocore.exceptions import ClientError

# AWS SES client creation (commented for now)
# ses_client = boto3.client('ses', region_name="us-east-1")

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
                "body": json.dumps({
                    "error": "receiver_email, subject, and body_text are required."
                })
            }

        # Mock email sending (replace with AWS SES later)
        print(f"[MOCK] Sending email to: {receiver_email}")
        print(f"Subject: {subject}")
        print(f"Body: {body_text}")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"Email to {receiver_email} with subject '{subject}' received!",
                "body_text": body_text
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
