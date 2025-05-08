from typing import Literal
from pydantic import BaseModel

class ResponseDto(BaseModel):
    status: Literal["success", "error"]
    message: str
