from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from app.database.connection import Base

class Resume(Base):

    __tablename__ = "resumes"

    id = Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    candidate = Column("candidate", String, ForeignKey("candidates.id"), nullable=False)
    email = Column("email", String, nullable=False)
    vaga = Column("vaga", String, nullable=False)
    email_text = Column("email_text", String)
    data = Column("data", String, nullable=False)
    createdAt = Column("createdAt", DateTime, default=datetime.now(timezone.utc))

    def __init__(self, candidate, email, data, vaga, email_text=None):
        self.candidate = candidate
        self.email = email
        self.vaga = vaga
        self.email_text = email_text
        self.data = data
