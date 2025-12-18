#!/bin/bash
set -euo pipefail

STACK_NAME="pdftools-dev"
PROFILE="dev"
REGION=${AWS_REGION:-"us-east-2"}

echo "Deploying to DEV stack: ${STACK_NAME} in ${REGION} using profile ${PROFILE}..."

sam deploy \
    --stack-name "${STACK_NAME}" \
    --profile "${PROFILE}" \
    --region "${REGION}" \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM\
    --resolve-s3 \
    --no-confirm-changeset
