from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.models.box import Box


class RequestCharacterUser(Base):
    __tablename__ = "request_character_user"
    user_id = Column(Integer, ForeignKey("users.id"))
    request_character_id = Column(Integer, ForeignKey("request_character.id"))
    ref_data = Column(String)
    status = Column(Boolean)

    __mapper_args__ = {
        "primary_key": ['user_id', 'request_character_id', 'ref_data']
    }


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
