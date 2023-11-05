from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, JSON
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.models.box import Box


class HistoryUser(Base):
    __tablename__ = "history_user"
    user_id = Column(Integer, ForeignKey("users.id"))
    history_id = Column(Integer, ForeignKey("history.id"))
    ref_data = Column(String)
    status = Column(Boolean)

    __mapper_args__ = {
        "primary_key": ['user_id', 'history_id', 'ref_data']
    }

    def reset(self, db, user_id):
        data = db.query(HistoryUser) \
            .filter_by(user_id=user_id) \
            .all()

        for d in data:
            db.delete(d)

        db.commit()


class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
