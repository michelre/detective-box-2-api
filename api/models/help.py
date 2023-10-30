from typing import List

from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.enums import HelpStatus


class Help(Base):
    __tablename__ = "help"

    id = Column(Integer, primary_key=True, index=True)
    ref = Column(String)
    title = Column(String)
    status = Column(Enum(HelpStatus))
    hints = Column(JSONB, default='[]')
    box_id = Column(Integer, ForeignKey('box.id'))
