from typing import List
from pydantic import BaseModel, EmailStr
from typing import Optional

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str = None

class CandidateResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str

    class Config:
        from_attributes = True



# Schema com dados opcionais para atualização
class CandidateUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None



class CandidatePaginatedResponse(BaseModel):
    page: int
    limit: int
    count: int
    total_candidates: int
    candidates: List[CandidateResponse]

    class Config:
        from_attributes = True