# 定义一个带路径参数的 GET 请求路由
from fastapi import APIRouter

from pydantic import BaseModel
user = APIRouter()

@user.get("/list")
async def read_item():
    return {"name": "xiaoli", "age": 10}



class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@user.put("/items/{item_id}")
async def update_item(item_id: bool, item: Item):
    results = {"item_id": item_id, "item": item}
    return results