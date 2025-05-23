import os

DEST_EMAIL = os.environ.get("EMAIL_DESTINATARIO", "contato@ponte-tech.com.br")
SES_SOURCE_EMAIL = os.environ.get("SES_SOURCE_EMAIL", "contato@ponte-tech.com.br")
USER_POOL_ID = os.environ.get("USER_POOL_ID", "us-east-1_NtC5KY3kF")

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",  
    "Access-Control-Allow-Headers": "Content-Type,Authorization",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
    "Access-Control-Allow-Credentials": "true"
}