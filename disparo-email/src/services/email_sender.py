from src.dto.request_dto import ContactRequestDto
from src.dto.service_dto import EmailDataDto

def format_email(contact: ContactRequestDto) -> EmailDataDto:
    body = (
        f"Nome: {contact.nomeCompleto}\n"
        f"E-mail: {contact.email}\n"
        f"Telefone: {contact.telefone}\n"
        f"Empresa: {contact.empresa}\n"
        f"Mensagem:\n{contact.mensagem}"
    )
    return EmailDataDto(
        to_address="contato@ponte-tech.com.br",
        subject="Nova mensagem do formulário de contato",
        body=body
    )
