import boto3
from botocore.exceptions import BotoCoreError, ClientError
from src.dto.service_dto import EmailDataDto

def send_email_via_ses(email_data: EmailDataDto) -> None:
    ses = boto3.client("ses")
    try:
        ses.send_email(
            Source="contato@ponte-tech.com.br",
            Destination={"ToAddresses": [email_data.to_address]},
            Message={
                "Subject": {"Data": email_data.subject},
                "Body": {
                    "Text": {"Data": email_data.body}
                }
            }
        )
    except (BotoCoreError, ClientError) as e:
        raise Exception(f"Erro ao enviar e-mail: {str(e)}")