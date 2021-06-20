from fastapi import APIRouter


router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.get("/detail/{id}", summary="User Details", description="Returns details of an user.")
async def root():
    return {"detail": "Hello World"}


@router.post("/detail/{id}", summary="User Details", description="Returns details of an user.")
async def root():
    return {"detail": "Hello World"}


@router.post("/register", summary="User Registration", description="Registers a new user.")
async def root():
    return {"detail": "This is POST method."}
