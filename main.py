from fastapi import FastAPI

from routers.exception import UnicornException
from routers.user.url import user
from routers.shop.url import shop
from routers.stream.url import stream
from routers.cookie.url import cookie
from routers.header.url import header
from routers.response_model.url import response_model
from routers.error.url import error

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
##https://fastapi.tiangolo.com/zh/tutorial/schema-extra-example/#pydantic-schema_extra
app = FastAPI()


app.include_router(user, prefix="/user", tags=["users"])
app.include_router(shop, prefix="/shop", tags=["shopping"])
app.include_router(stream, prefix="/stream", tags=["streaming return"])
app.include_router(cookie, prefix="/cookie", tags=["cookie"])
app.include_router(header, prefix="/header", tags=["header"])
app.include_router(response_model, prefix="/response_model", tags=["response model"])
app.include_router(error, prefix="/error", tags=["error"])



@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


# 启动应用（用于直接运行）
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)