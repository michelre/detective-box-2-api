from sqlalchemy import Column, Integer, String,Enum, ForeignKey
from api.enums import ObjectiveStatus

from api.database import Base


class UserBox(Base):
    __tablename__ = "user_box"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    box_id = Column(Integer, ForeignKey("box.id"), primary_key=True)
    status = Column(String)

class Box(Base):
    __tablename__ = "box"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cover = Column(String, nullable=True)
    status = Column(Enum(ObjectiveStatus), nullable=True)
