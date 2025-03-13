from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    date: str
    time: str
    location: str
    coordinator: str
    status: str = "upcoming"