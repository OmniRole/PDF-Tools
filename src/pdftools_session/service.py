import os
import time
import uuid
import boto3
from botocore.exceptions import ClientError
from botocore.config import Config


from constants import (
    DEFAULT_PRESIGN_EXPIRES_SECONDS,
    DEFAULT_SESSION_TTL_SECONDS,
    ENV_BUCKET_NAME,
    ENV_SESSIONS_TABLE,
    S3_SESSION_PREFIX,
)
from models import session_response_dict

_s3 = boto3.client(
    "s3",
    region_name="us-east-2",
    config=Config(signature_version='s3v4')
)
_ddb = boto3.resource("dynamodb")

def create_session(req: dict) -> dict:
    session_id = str(uuid.uuid4())
    now = int(time.time())
    expires_at = now + DEFAULT_SESSION_TTL_SECONDS


    session_prefix = f"{S3_SESSION_PREFIX}/{session_id}/"
    

    key_pattern = f"{session_prefix}${{filename}}"

    try:
        presigned_post = _s3.generate_presigned_post(
            Bucket=ENV_BUCKET_NAME,
            Key=key_pattern,
            Conditions=[
                ["starts-with", "$key", session_prefix],
                {"Content-Type": "application/pdf"},
                ["content-length-range", 1, 52428800] # Limit: 1 byte to 50MB
            ],
            ExpiresIn=DEFAULT_PRESIGN_EXPIRES_SECONDS,
        )
    except ClientError as e:
        print(f"Error generating presigned post: {e}")
        raise


    item = {
        "sessionId": session_id,
        "ttl": expires_at,
        "createdAt": now,
        "bucket": ENV_BUCKET_NAME,
        "s3Prefix": session_prefix, # Store the folder so the merger knows where to look
    }

    if isinstance(req, dict) and req.get("user_id"):
        item["userId"] = req.get("user_id")

    table = _ddb.Table(ENV_SESSIONS_TABLE)
    table.put_item(Item=item, ConditionExpression="attribute_not_exists(sessionId)")


    return {
        "sessionId": session_id,
        "expiresAt": expires_at,
        "upload": {
            "url": presigned_post["url"],
            "fields": presigned_post["fields"]
        }
    }