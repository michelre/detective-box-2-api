from sqlalchemy import Column, Integer, String,Enum, ForeignKey
from api.enums import ObjectiveStatus

from api.database import Base


class UserBox(Base):
    __tablename__ = "user_box"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    box_id = Column(Integer, ForeignKey("box.id"), primary_key=True)
    status = Column(String)

    def reset(self, db, user_id):
        boxes = db.query(UserBox).filter_by(user_id=user_id).all()
        for box in boxes:
            db.delete(box)

        db.commit()


class Box(Base):
    __tablename__ = "box"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    cover = Column(String, nullable=True)
    status = Column(Enum(ObjectiveStatus), nullable=True)
