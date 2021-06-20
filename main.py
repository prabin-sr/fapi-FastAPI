# python modules
import time
import logging  # TODO

# third-party modules
import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# user-defined modules
from settings.base import conn
from settings.base import settings
# import all routers here
from users import routers as user_routers


# app specifications
app = FastAPI(title="MyApp", description="APIs for MyApp", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS,
)


# TODO
# @app.middleware("http")
# async def request_logger(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     print(process_time)
#     return response


# TODO
# Authentication Middleware


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#     )


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


# register all router objects here
app.include_router(user_routers.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT,
                reload=settings.RELOAD, workers=settings.WORKERS)
