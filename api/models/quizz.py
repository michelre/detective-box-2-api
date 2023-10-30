from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from api.models.box import Box
from api.database import Base


class Quizz(Base):
    __tablename__ = "quizz"

    id = Column(Integer, primary_key=True, index=True)
    questions = Column(JSONB, default='[]')
    answers = Column(JSONB, default='[]')
    status = Column(Boolean, default=False)
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
