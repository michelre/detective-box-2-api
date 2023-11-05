from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Enum
from sqlalchemy.dialects.postgresql import JSONB

from api.database import Base
from api.enums import HelpStatus


class HelpUser(Base):
    __tablename__ = "help_user"
    user_id = Column(Integer, ForeignKey("users.id"))
    help_id = Column(Integer, ForeignKey("help.id"))
    ref_data = Column(String)
    status = Column(Enum(HelpStatus))

    __mapper_args__ = {
        "primary_key": ['user_id', 'help_id', 'ref_data']
    }

class Help(Base):
    __tablename__ = "help"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB, default=[])
    box_id = Column(Integer, ForeignKey('box.id'))
