from datetime import date
from pydantic import BaseModel, ConfigDict
from .models import Status


class ApplicationCreate(BaseModel):
    company: str
    role: str
    portal: str | None = None
    status: Status = Status.applied
    applied_date: date | None = None
    notes: str | None = None


class ApplicationUpdate(BaseModel):
    company: str | None = None
    role: str | None = None
    portal: str | None = None
    status: Status | None = None
    notes: str | None = None


class ApplicationOut(ApplicationCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    applied_date: date