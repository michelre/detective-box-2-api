from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.models.box import Box


class HistoryUser(Base):
    __tablename__ = "history_user"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    history_id = Column(Integer, ForeignKey("history.id"), primary_key=True)
    ref_data = Column(String)
    status = Column(Boolean)


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
