import json
from .models import MergeRequest
from .service import MergeService

def lambda_handler(event, context):
    try:
        body_str = event.get("body", "{}")
        body = json.loads(body_str) if body_str else {}
        
        request = MergeRequest.from_dict(body)
        service = MergeService()
        response_model = service.merge_pdfs(request)
        
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(response_model.to_dict())
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
