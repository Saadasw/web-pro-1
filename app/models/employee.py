from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    position = Column(String, nullable=False)  # Example: "AI Engineer"
    services_offered = Column(Text)  # Comma-separated services: "AI Agents, Odoo, IoT"
    linkedin_url = Column(String, nullable=True)
    github_url = Column(String, nullable=True)

    user = relationship("User", back_populates="employee_profile")  # Link to User model
