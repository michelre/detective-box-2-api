from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.models.box import Box


class RequestCharacter(Base):
    __tablename__ = "request_character"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB)
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
    character_id = Column(Integer, ForeignKey("character.id"))


class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sound = Column(String)
