# 定义一个带路径参数的 GET 请求路由
from fastapi import APIRouter

from routers.exception import UnicornException

error = APIRouter()




@error.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


