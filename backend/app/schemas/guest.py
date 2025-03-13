from pydantic import BaseModel, EmailStr
from typing import Optional

class GuestBase(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None
    type: str
    rsvp_status: str = "pending"
    special_requirements: Optional[str] = None

class GuestCreate(GuestBase):
    pass

class GuestUpdate(GuestBase):
    pass

class Guest(GuestBase):
    id: int

    class Config:
        orm_mode = True