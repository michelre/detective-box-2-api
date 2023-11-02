from pydantic import BaseModel, ConfigDict

from api.enums import EventStatus as Status


class Event(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)


class EventStatus(BaseModel):
    status: Status
