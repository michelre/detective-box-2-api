from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship, Mapped

from api.database import Base
from api.models.box import Box


class QuizzUser(Base):
    __tablename__ = "quizz_user"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    quizz_id = Column(Integer, ForeignKey("quizz.id"), primary_key=True)
    status = Column(Boolean)

    def reset(self, db, user_id):
        quizzs = db.query(QuizzUser) \
            .filter_by(user_id=user_id) \
            .all()

        for q in quizzs:
            db.delete(q)

        db.commit()


class Quizz(Base):
    __tablename__ = "quizz"

    id = Column(Integer, primary_key=True, index=True)
    questions = Column(JSONB, default='[]')
    answers = Column(JSONB, default='[]')
    box_id = Column(Integer, ForeignKey("box.id"))
    box: Mapped[Box] = relationship("Box")
