import boto3
import uuid
from src.dto.request_dto import ContactRequestDto

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("envio_contato")

def save_contact_to_dynamodb(contact: ContactRequestDto) -> None:
    item = {
        "id_contato": str(uuid.uuid4()), 
        "email": contact.email, 
        "nomeCompleto": contact.nomeCompleto,
        "telefone": contact.telefone,
        "empresa": contact.empresa,
        "mensagem": contact.mensagem
    }
    table.put_item(Item=item)