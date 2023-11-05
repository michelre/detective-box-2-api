from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.models.box import Box


class ObjectiveUser(Base):
    __tablename__ = "objective_user"
    user_id = Column(Integer, ForeignKey("users.id"))
    objective_id = Column(Integer, ForeignKey("objective.id"))
    ref_data = Column(Integer)
    status = Column(String)

    __mapper_args__ = {
        "primary_key": ['user_id', 'objective_id', 'ref_data']
    }


class Objective(Base):
    __tablename__ = "objective"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB)
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
