from pydantic import ConfigDict, BaseModel
from api.enums import BoxStatus


class Box(BaseModel):
    id: int
    name: str
    cover: str | None
    status: BoxStatus
    model_config = ConfigDict(from_attributes=True)


class BoxStatus(BaseModel):
    status: BoxStatus
