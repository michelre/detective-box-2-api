from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    name: str
    pass


class User(UserCreate):
    id: int

    class Config:
        orm_mode = True
