from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.models.box import Box


class ObjectiveUser(Base):
    __tablename__ = "objective_user"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    objective_id = Column(Integer, ForeignKey("objective.id"), primary_key=True)
    ref_data = Column(Integer,  primary_key=True)
    status = Column(String)


class Objective(Base):
    __tablename__ = "objective"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB)
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
