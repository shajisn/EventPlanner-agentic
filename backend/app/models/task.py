from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from ..db.session import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    coordinator = Column(String, nullable=False)
    deadline = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    status = Column(String, default='pending')

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, status={self.status})>"