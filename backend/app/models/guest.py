from pydantic import BaseModel, EmailStr
from typing import Optional

class Guest(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    company: Optional[str] = None
    type: str
    rsvp_status: str = "pending"
    special_requirements: Optional[str] = None

    class Config:
        orm_mode = True