from pydantic import ConfigDict, BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserBase):
    name: str
    pass


class User(UserCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
