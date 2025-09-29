# 定义一个带路径参数的 GET 请求路由
from fastapi import APIRouter, Header
from typing import Annotated
header = APIRouter()


@header.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent} # 神奇的是 浏览器是 User-Agent 也能接收到

@header.get("/items2/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}