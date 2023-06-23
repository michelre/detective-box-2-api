from pydantic import BaseModel


class Status(BaseModel):
    status: str


class User(BaseModel):
    id: int
    login: str
    password: str

    class Config:
        orm_mode = True
