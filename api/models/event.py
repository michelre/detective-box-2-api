from typing import List

from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.enums import HelpStatus


class EventUser(Base):
    __tablename__ = "event_user"
    user_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("event.id"))
    ref_data = Column(Integer)
    status = Column(String)

    __mapper_args__ = {
        "primary_key": ['user_id', 'event_id', 'ref_data']
    }


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB, default=[])
    box_id = Column(Integer, ForeignKey('box.id'))
