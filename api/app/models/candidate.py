from datetime import datetime, timezone
import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from app.database.connection import Base


class Candidate(Base):

    __tablename__= "candidates"

    id = Column("id", String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = Column("name", String)
    email = Column("email", String, nullable=False, unique=True)
    phone = Column("phone", String)
    createdAt = Column("createdAt", DateTime, default=datetime.now(timezone.utc))

    def __init__(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

