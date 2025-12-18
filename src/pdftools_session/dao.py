from typing import Any, Dict

def create_session_stub(self, user_id: str) -> Dict[str, Any]:
        """Stub method returns fake session data."""
        return {
            "session_id": f"sess_{user_id}_999",
            "status": "active"
        }
