import enum
from datetime import date
from sqlalchemy import String, Date, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Status(str, enum.Enum):
    applied = "applied"
    interview = "interview"
    offer = "offer"
    rejected = "rejected"


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    company: Mapped[str] = mapped_column(String(100), index=True)
    role: Mapped[str] = mapped_column(String(100))
    portal: Mapped[str | None] = mapped_column(String(50))
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.applied)
    applied_date: Mapped[date] = mapped_column(Date, default=date.today)
    notes: Mapped[str | None] = mapped_column(Text)