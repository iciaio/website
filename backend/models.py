import datetime
import datetime as _dt
import sqlalchemy as _sql
from sqlalchemy.orm import Mapped

import database as _db


class Content(_db.Base):
    __tablename__ = "content"
    id: str = _sql.Column(_sql.Integer, primary_key=True, index=True)
    date: datetime.datetime = _sql.Column(_sql.DateTime, default=_dt.datetime.utcfromtimestamp(0))
    description: str = _sql.Column(_sql.String, index=True)
    s3_documentation: str = _sql.Column(_sql.String)
    title: str = _sql.Column(_sql.String, nullable=True)


class Project(_db.Base):
    __tablename__ = "projects"
    id: str = _sql.Column(_sql.Integer, primary_key=True, index=True)
    project_title: str = _sql.Column(_sql.String, index=True)
    content_id: str = _sql.Column(_sql.Integer, _sql.ForeignKey('content.id'))
    tags: Mapped[int] = _sql.Column(_sql.ARRAY(_sql.String))
