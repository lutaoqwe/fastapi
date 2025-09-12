# 定义一个带路径参数的 GET 请求路由
from fastapi import APIRouter

user = APIRouter()

@user.get("/list")
async def read_item():
    return {"name": "xiaoli", "age": 10}
