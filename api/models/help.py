from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Enum
from sqlalchemy.dialects.postgresql import JSONB

from api.database import Base
from api.enums import HelpStatus


class HelpUser(Base):
    __tablename__ = "help_user"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    help_id = Column(Integer, ForeignKey("help.id"), primary_key=True)
    ref_data = Column(String,  primary_key=True)
    status = Column(Enum(HelpStatus))

class Help(Base):
    __tablename__ = "help"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB, default=[])
    box_id = Column(Integer, ForeignKey('box.id'))
