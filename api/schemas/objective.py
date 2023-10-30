from pydantic import ConfigDict, BaseModel
from api.enums import BoxStatus


class Objective(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)
