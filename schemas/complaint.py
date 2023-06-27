from datetime import datetime

from pydantic import BaseModel

from models.enums import ComplaintState


class BaseComplaint(BaseModel):
    title: str
    description: str
    photo_url: str
    amount: float


class ComplaintIn(BaseComplaint):
    pass


class ComplaintOut(BaseComplaint):
    id: int
    create_date: datetime
    status: ComplaintState
