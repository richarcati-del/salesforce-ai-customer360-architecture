import json
import boto3
from datetime import datetime

eventbridge = boto3.client("events")

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    customer_event = {
        "customerId": body.get("customerId"),
        "eventType": body.get("eventType"),
        "campaignId": body.get("campaignId"),
        "pageUrl": body.get("pageUrl"),
        "timestamp": datetime.utcnow().isoformat()
    }

    eventbridge.put_events(
        Entries=[
            {
                "Source": "website.personalization",
                "DetailType": "CustomerEngagementEvent",
                "Detail": json.dumps(customer_event),
                "EventBusName": "customer360-event-bus"
            }
        ]
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Event published successfully"})
    }
