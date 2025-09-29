# 定义一个带路径参数的 GET 请求路由
from fastapi import APIRouter, Cookie
from pydantic import BaseModel
from typing import Annotated
cookie = APIRouter()

@cookie.get("/list")
async def read_item():
    return {"name": "xiaoli", "age": 10}


@cookie.get("/items")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}


class Cookies(BaseModel):
    session_id: str
    name: str | None = None
    email: str | None = None


@cookie.get("/cookies2/")
async def get_cookie1(cookies: Annotated[Cookies, Cookie()]):#带cookie教研
    for cookie in cookies:
        print(cookie)
    return cookies