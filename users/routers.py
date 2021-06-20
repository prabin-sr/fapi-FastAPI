from fastapi import APIRouter

from . import functions


router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.get("/detail/{id}", summary="User Details", description="Returns details of an user.")
async def root():
    user_id = await functions.create_db_values()
    return {"detail": f"Hello World {user_id}"}


@router.post("/detail/{id}", summary="User Details", description="Returns details of an user.")
async def root():
    return {"detail": "Hello World"}


@router.post("/register", summary="User Registration", description="Registers a new user.")
async def root():
    return {"detail": "This is POST method."}
