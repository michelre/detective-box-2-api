from sqlalchemy import Column, String, Integer, DateTime

from api.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    end_box1 = Column(DateTime)
    end_box2 = Column(DateTime)
    end_box3 = Column(DateTime)
    # boxes: Mapped[List[Box]] = relationship(UserBox)
