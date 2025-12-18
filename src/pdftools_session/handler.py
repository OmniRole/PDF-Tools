# src/pdftools_session/handler.py
import base64
import json
import logging

from models import parse_session_request
from service import create_session

logger = logging.getLogger()
logger.setLevel(logging.INFO)



def _resp(status_code: int, body: dict) -> dict:
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def lambda_handler(event, context):
    request_id = getattr(context, "aws_request_id", None)

    try:
        body_str = event.get("body") or ""
        if event.get("isBase64Encoded"):
            body_str = base64.b64decode(body_str).decode("utf-8")

        if not body_str.strip():
            payload = {}
        else:
            try:
                payload = json.loads(body_str)
            except json.JSONDecodeError:
                return _resp(400, {"error": "Invalid JSON body", "code": "BAD_JSON"})

        response = create_session(payload)

        # If service returns a dict already (recommended with this minimal approach)
        if isinstance(response, dict):
            return _resp(201, response)

        # If service still returns an object with to_dict()
        if hasattr(response, "to_dict"):
            return _resp(201, response.to_dict())

        # Fallback: return as-is
        return _resp(201, response)

    except Exception:
        logger.exception("Unhandled error in session handler (request_id=%s)", request_id)
        return _resp(500, {"error": "Internal Server Error", "code": "INTERNAL"})
