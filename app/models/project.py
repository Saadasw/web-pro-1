from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    service_id = Column(Integer, ForeignKey("services.id"))  # Links project to a service

    service = relationship("Service", back_populates="projects")  # Establishes relationship
