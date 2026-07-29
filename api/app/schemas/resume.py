from pydantic import BaseModel, EmailStr
from typing import Optional

class ResumeCreate(BaseModel):
    name: str
    email: str
    phone: str
    vaga: str
    email_text: str = None
    data: str



class ResumeResponse(BaseModel):
    id: str
    candidate: str
    vaga: str
    email_text: str
    data: str

    class Config:
        from_attributes = True



# Schema com dados opcionais para atualização
class CandidateUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None






