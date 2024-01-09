import datetime
import datetime as _dt
from typing import List

import sqlalchemy as _sql
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
import sqlalchemy.ext.declarative as _declarative

Base = _declarative.declarative_base()


class Content(Base):
    __tablename__ = "content"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    date: Mapped[datetime.datetime] = mapped_column(default=_dt.datetime.utcfromtimestamp(0))
    description: Mapped[str] = mapped_column(index=True)
    s3_documentation: Mapped[str] = mapped_column(nullable=True)
    title: Mapped[str] = mapped_column(nullable=True)
    project_id: Mapped[int] = mapped_column(_sql.ForeignKey("projects.id"))


class Project(Base):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    project_title: Mapped[str] = mapped_column(index=True)
    tags: Mapped[List[str]] = mapped_column(_sql.ARRAY(_sql.String))
    content: Mapped[List["Content"]] = relationship()