from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # Store hashed password
    is_active = Column(Boolean, default=True)  # User status
    is_admin = Column(Boolean, default=False)  # Admin privilege
