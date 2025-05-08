import json
from src.dto.request_dto import ContactRequestDto
from src.dto.response_dto import ResponseDto
from src.services.email_sender import format_email
from repositories.email_sender import send_email_via_ses

def handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        contact = ContactRequestDto(**body)

        email_data = format_email(contact)
        send_email_via_ses(email_data)

        response = ResponseDto(status="success", message="Email enviado com sucesso.")
        print("✅ E-mail enviado com sucesso.")
        return {
            "statusCode": 200,
            "body": response.json()
        }

    except Exception as e:
        print(f"❌ Erro: {str(e)}")
        response = ResponseDto(status="error", message=str(e))
        return {
            "statusCode": 400,
            "body": response.json()
        }