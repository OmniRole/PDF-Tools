# src/pdftools_session/models.py
from typing import Any, Dict, Optional


def parse_session_request(payload: Any) -> Dict[str, Optional[str]]:
    """
    Minimal request parser.
    Accepts optional userId/user_id; everything else is ignored.
    """
    if not isinstance(payload, dict):
        return {"user_id": None}

    raw_user = payload.get("userId", payload.get("user_id"))
    user_id = str(raw_user).strip() if raw_user is not None else None
    return {"user_id": user_id or None}


def session_response_dict(session_id: str, expires_at: int, upload_url: str) -> Dict[str, Any]:
    """
    Minimal response builder.
    """
    return {
        "sessionId": session_id,
        "expiresAt": expires_at,
        "uploadUrl": upload_url,
        "status": "CREATED",
    }
