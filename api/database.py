from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from api.config import settings

DATABASE_URI = settings.database_uri

engine = create_engine(
    DATABASE_URI,
    pool_size=20,
    max_overflow=-1
)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        db.rollback()  # Rollback on exception
        raise e
    finally:
        db.close()

def close_database_connections():
    print("closing all connections to the database")
    engine.dispose()
