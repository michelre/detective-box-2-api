from pydantic import BaseModel, ConfigDict

from api.enums import HelpStatus


class Help(BaseModel):
    id: int
    ref: str
    title: str
    status: HelpStatus
    hints: str
    box_id: int
    model_config = ConfigDict(from_attributes=True)


class Status(BaseModel):
    status: HelpStatus
