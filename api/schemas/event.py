from pydantic import BaseModel, ConfigDict

from api.enums import HelpStatus


class Event(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)

