from pydantic import ConfigDict, BaseModel


class History(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)
