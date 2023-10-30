from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.models.box import Box


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
