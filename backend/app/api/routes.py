import sqlalchemy.orm as _orm
import fastapi as _fastapi
import app.api.models as _models
from app.services import services

router = _fastapi.APIRouter()


# mock_projects = {
#     1: {
#         "project_title": "The Girls Are Home",
#         "tags": ["augmented reality", "sculpture", "memory", "experimental capture", "time based"],
#         "content": {
#             "date": _datetime.datetime(2017, 5, 11),
#             "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus porttitor turpis in magna dapibus consequat. Quisque quam justo, suscipit non elit in, ullamcorper mattis urna. Integer non pretium quam. Morbi nec libero sit amet odio egestas ornare. Donec tempus sem mattis odio consequat, a consequat arcu dictum. Nam et nisi vulputate, venenatis enim et, molestie urna. Donec vehicula ligula euismod ultricies fermentum. Suspendisse potenti. Nunc ut tincidunt quam, vel ultricies nisi. Ut vitae pulvinar nibh, in iaculis diam. Aenean tristique nibh in diam aliquam, ac facilisis est posuere. Nam ac magna eu nibh pretium maximus nec non augue. Donec et mattis ex, in vehicula mauris. Nam leo neque, malesuada a mi et, convallis fringilla odio. Aliquam fermentum, erat ut venenatis mattis, libero leo pulvinar lacus, vel ultricies mi ante vitae sapien. Vivamus iaculis arcu tellus, hendrerit cursus est tempor quis.",
#             "documentation": "",
#         }
#     },
#     2: {
#         "project_title": "Gouache Paintings",
#         "tags": ["painting", "memory"],
#         "content": [
#             {
#                 "title": "A clock in the works!",
#                 "date": _datetime.datetime(2019, 11, 5),
#                 "description": "Nunc ut augue ipsum. Sed molestie ex non erat consectetur, quis mollis turpis tincidunt. Phasellus lectus nibh, accumsan ut urna sit amet, luctus imperdiet quam. Integer dictum dapibus felis id mollis. Aenean fermentum, elit a viverra dignissim, justo nibh accumsan dui, at ultrices nunc nunc ut sem. Pellentesque non nisl urna. Pellentesque viverra interdum porta. Donec a elit quis tortor venenatis tristique non quis quam. Ut ac orci ornare, ornare erat sed, convallis eros.",
#                 "documentation": "",
#             },
#             {
#                 "title": "A master never pieces out",
#                 "date": _datetime.datetime(2020, 10, 9),
#                 "description": "Nunc ut augue ipsum. Sed molestie ex non erat consectetur, quis mollis turpis tincidunt. Phasellus lectus nibh, accumsan ut urna sit amet, luctus imperdiet quam. Integer dictum dapibus felis id mollis. Aenean fermentum, elit a viverra dignissim, justo nibh accumsan dui, at ultrices nunc nunc ut sem. Pellentesque non nisl urna. Pellentesque viverra interdum porta. Donec a elit quis tortor venenatis tristique non quis quam. Ut ac orci ornare, ornare erat sed, convallis eros.",
#                 "documentation": "",
#             },
#             {
#                 "title": "Baby brought the buns",
#                 "date": _datetime.datetime(2018, 8, 7),
#                 "description": "Nunc ut augue ipsum. Sed molestie ex non erat consectetur, quis mollis turpis tincidunt. Phasellus lectus nibh, accumsan ut urna sit amet, luctus imperdiet quam. Integer dictum dapibus felis id mollis. Aenean fermentum, elit a viverra dignissim, justo nibh accumsan dui, at ultrices nunc nunc ut sem. Pellentesque non nisl urna. Pellentesque viverra interdum porta. Donec a elit quis tortor venenatis tristique non quis quam. Ut ac orci ornare, ornare erat sed, convallis eros.",
#                 "documentation": "",
#             }
#         ]
#     },
# }

# @app.post("/api/projects", response_model=_schemas.Project)
@router.post("/api/projects", response_model=_models.Project)
async def create_project(
        project: _models.CreateProject,
        db: _orm.session = _fastapi.Depends(services.db_session)
):
    return await services.create_project(project, db)

# @app.get("/api/project/{id}")
# def get_project(id: int):
#     try:
#         return mock_projects[id]
#     except KeyError:
#         raise HTTPException(
#             status_code=404, detail=f"Project with id {id} was not found."
#         )
#
#
# @app.post("api/project", status_code=status.HTTP_201_CREATED)
# def create_project(project: Project):
#     project_id = max(mock_projects.keys()) + 1
#     mock_projects[project_id]: project.model_dump
#     return mock_projects[project_id]
