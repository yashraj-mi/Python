from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from contextlib import  contextmanager
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")


engine = create_engine(DATABASE_URL)
load_dotenv()


sessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

class  Base(DeclarativeBase):
    pass


@contextmanager
def get_session():
    session=sessionLocal()
    try:
        yield session
        session.commit()

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()