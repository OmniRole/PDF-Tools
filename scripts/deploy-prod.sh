#!/bin/bash
set -euo pipefail

STACK_NAME="pdftools-prod"
PROFILE="prod"
REGION=${AWS_REGION:-"us-east-2"}

echo "Deploying to PROD stack: ${STACK_NAME} in ${REGION} using profile ${PROFILE}..."

sam deploy \
    --stack-name "${STACK_NAME}" \
    --profile "${PROFILE}" \
    --region "${REGION}" \
    --capabilities CAPABILITY_IAM \
    --resolve-s3 \
    --confirm-changeset
