from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)     
    password = Column(String(255), nullable=False)              
    is_deleted = Column(Boolean, default=False)


