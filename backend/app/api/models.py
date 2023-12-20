import datetime as _dt
from typing import List, Union

import pydantic as _pydantic


class _BaseContent(_pydantic.BaseModel):
    date: _dt.datetime
    description: str
    s3_documentation: Union[str, None]
    title: Union[str, None]


class Content(_BaseContent):
    id: int
    project_id: int


class _BaseProject(_pydantic.BaseModel):
    project_title: str
    tags: List[str]
    content: Union[_BaseContent, List[_BaseContent]]


class Project(_BaseProject):
    id: int


class CreateProject(_BaseProject):
    pass
