from pydantic import BaseModel

class EmailDataDto(BaseModel):
    to_address: str
    subject: str
    body: str
