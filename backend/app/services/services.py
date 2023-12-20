from app.database import models as _db_models, session as _database
from app.api import models as _api_models
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _db_models.Base.metadata.create_all(bind=_database.engine)


def db_session():
    _db = _database.SessionLocal()
    try:
        yield _db
    finally:
        _db.close()


async def create_project(
        project: _api_models.CreateProject, _db_session: "Session"
) -> _api_models.Project:
    project = _api_models.Project(**project.model_dump())
    print("-------------")
    print(project)
    _db_session.add(project)
    _db_session.commit()
    _db_session.refresh(project)
    return _api_models.Project.from_orm(project)
