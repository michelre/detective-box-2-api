from pydantic import ConfigDict, BaseModel
from api.enums import BoxStatus


class Quizz(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)


class QuizzStatus(BaseModel):
    status: bool

