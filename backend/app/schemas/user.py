from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str = None

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True