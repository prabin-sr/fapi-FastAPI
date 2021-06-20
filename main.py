# third-party modules
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# user-defined modules
from settings.base import conn
from settings.base import settings
from users import routers as user_routers
# TODO: import all routers here


# app specifications
app = FastAPI(title="MyApp", description="API's for MyApp", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS,
)


@app.on_event("startup")
async def startup():
    print("Initiating Database Connection...")
    if conn.is_closed():
        conn.connect()


@app.on_event("shutdown")
async def shutdown():
    print("Closing Database Connection...")
    if not conn.is_closed():
        conn.close()


app.include_router(user_routers.router)
# TODO: register all router objects here


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT,
                reload=settings.RELOAD, workers=settings.WORKERS)
