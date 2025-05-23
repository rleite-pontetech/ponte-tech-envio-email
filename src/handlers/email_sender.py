import json
from src.dto.request_dto import ContactRequestDto
from src.dto.response_dto import ResponseDto
from src.services.email_sender import format_email
from src.repositories.email_sender import send_email_via_ses
from src.repositories.dynamo_sender import save_contact_to_dynamodb
from src.config.settings import CORS_HEADERS

def handler(event, context):
    try:
        method = event.get("requestContext", {}).get("http", {}).get("method", "")
        if method == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": CORS_HEADERS,
                "body": json.dumps({"message": "CORS preflight check OK"})
            }

        body = json.loads(event.get("body", "{}"))
        contact = ContactRequestDto(**body)

        save_contact_to_dynamodb(contact)

        email_data = format_email(contact)
        send_email_via_ses(email_data)

        response = ResponseDto(status="success", message="Email enviado com sucesso.")
        print("✅ E-mail enviado com sucesso.")
        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": response.json()
        }

    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        response = ResponseDto(status="error", message=str(e))
        return {
            "statusCode": 400,
            "headers": CORS_HEADERS,
            "body": response.json()
        }
