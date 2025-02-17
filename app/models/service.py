from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)  # Example: "AI Agent Solutions"
    description = Column(Text, nullable=True)  # Detailed description of the service
