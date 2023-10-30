from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.enums import ObjectiveStatus
from api.models.box import Box


class Objective(Base):
    __tablename__ = "objective"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    subtitle = Column(String)
    detail = Column(Text)
    status = Column(Enum(ObjectiveStatus))
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
