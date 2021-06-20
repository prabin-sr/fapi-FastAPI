from fastapi import APIRouter, Response, status

from .validators import RegisterUserRequest
from .functions import (
    register_user,
    create_db_values,
)


router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.get("/detail/{id}", summary="User Details", description="Returns details of an user.")
async def root():
    user_id = await create_db_values()
    return {"detail": f"Hello World {user_id}"}


@router.post("/detail/{id}", summary="User Details", description="Returns details of an user.")
async def root():
    return {"detail": "Hello World"}


@router.post("/register", summary="User Registration", description="Registers a new user.", status_code=status.HTTP_201_CREATED)
async def register(request: RegisterUserRequest, response: Response):
    await register_user(request)
    response.status_code = status.HTTP_201_CREATED
    return {"detail": "user registration success."}
