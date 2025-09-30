from fastapi import Request
from fastapi.responses import JSONResponse

from routers.exception.exception import UnicornException


async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! {exc.name} did something. There goes a rainbow...",
            "code": 500
        },
    )