from pydantic import BaseModel, EmailStr, Field

class ContactRequestDto(BaseModel):
    nomeCompleto: str = Field(..., min_length=1)
    email: EmailStr
    telefone: str = Field(..., min_length=1)
    empresa: str = Field(..., min_length=1)
    mensagem: str = ""