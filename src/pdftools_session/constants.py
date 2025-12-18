# src/pdftools_session/constants.py

# Environment variable names
ENV_BUCKET_NAME = "omnirole-pdftools"
ENV_SESSIONS_TABLE = "omnirole-pdftools"


# Defaults
DEFAULT_SESSION_TTL_SECONDS = 3600          # 1 hour
DEFAULT_PRESIGN_EXPIRES_SECONDS = 900       # 15 minutes

# S3 key prefix
S3_SESSION_PREFIX = "sessions"