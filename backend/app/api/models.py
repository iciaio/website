import datetime as _dt
from typing import List, Union, Optional
from typing import Dict

import pydantic as _pydantic


class _BaseContent(_pydantic.BaseModel):
    date: _dt.datetime
    description: str
    s3_documentation: Optional[str]
    title: Optional[str]

    class Config:
        from_attributes = True


class Content(_BaseContent):
    id: int
    project_id: int


class _BaseProject(_pydantic.BaseModel):
    project_title: str
    tags: List[str]
    content: List[_BaseContent]


class Project(_BaseProject):
    id: int

    class Config:
        from_attributes = True


class CreateProject(_BaseProject):
    pass
