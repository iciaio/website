import datetime
import datetime as _dt
import sqlalchemy as _sql
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
import sqlalchemy.ext.declarative as _declarative

Base = _declarative.declarative_base()

class Content(Base):
    __tablename__ = "content"
    id: str = _sql.Column(_sql.Integer, primary_key=True, index=True)
    date: datetime.datetime = _sql.Column(_sql.DateTime, default=_dt.datetime.utcfromtimestamp(0))
    description: str = _sql.Column(_sql.String, index=True)
    s3_documentation: str = _sql.Column(_sql.String, nullable=True)
    title: str = _sql.Column(_sql.String, nullable=True)
    project_id = _sql.Column(_sql.Integer, _sql.ForeignKey("projects.id"))
    project = relationship("Project", back_populates="content")


class Project(Base):
    __tablename__ = "projects"
    id: str = _sql.Column(_sql.Integer, primary_key=True, index=True)
    project_title: str = _sql.Column(_sql.String, index=True)
    tags: Mapped[int] = _sql.Column(_sql.ARRAY(_sql.String))
    content = relationship("Content", back_populates="project")
