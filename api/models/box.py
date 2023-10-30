from sqlalchemy import Column, Integer, String,Enum
from api.enums import ObjectiveStatus

from api.database import Base


class Box(Base):
    __tablename__ = "box"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cover = Column(String, nullable=True)
    status = Column(Enum(ObjectiveStatus), nullable=True)
