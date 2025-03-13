from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./anniversary_app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    from ..models.user import User
    from ..models.event import Event
    from ..models.task import Task
    from ..models.guest import Guest

    Base.metadata.create_all(bind=engine)

    # Insert initial data if needed
    # This can be expanded based on your requirements
    with SessionLocal() as session:
        # Add initial users, events, tasks, and guests here
        pass