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
        project: _api_models.CreateProject, db: "Session"
) -> _api_models.Project:
    print(project);
    dumped_content = [_db_models.Content(**m.model_dump()) for m in project.content]
    db_project = _db_models.Project(
        project_title=project.project_title,
        tags=project.tags,
        content=dumped_content
    )

    # Add the SQLAlchemy model instance to the session
    db.add(db_project)

    # Commit the changes and refresh the instance to get the updated data
    db.commit()
    db.refresh(db_project)

    # Convert the SQLAlchemy model instance to a Pydantic model and return
    return _api_models.Project.model_validate(db_project)

