# 定义一个带路径参数的 GET 请求路由
from fastapi import APIRouter

shop = APIRouter()

@shop.get("/list")
async def read_item():
    return {"item_id": "shoo", "q": "shopssss"}
