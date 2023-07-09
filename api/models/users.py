from sqlalchemy import Column, String, Integer
from api.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
