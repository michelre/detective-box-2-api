from sqlalchemy.orm import relationship, Mapped
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, ForeignKey, Enum
from api.database import Base
from api.enums import BoxStatus
from api.models.box import Box

from typing import List


class UserBox(Base):
    __tablename__ = "user_box"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    box_id = Column(Integer, ForeignKey("box.id"), primary_key=True)
    status = Column(Enum(BoxStatus))



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    boxes: Mapped[List[Box]] = relationship(UserBox)
