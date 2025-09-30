# 定义一个带路径参数的 GET 请求路由
from fastapi import APIRouter, HTTPException

from routers.exception import UnicornException


error = APIRouter()




@error.get("/unicorns/{name}",
    summary="Create an unicorns"
)
async def read_unicorn(name: str):
    """
        Create an item with all the information:

        - **name**: each item must have a name
        - **description**: a long description
        - **price**: required
        - **tax**: if the item doesn't have tax, you can omit this
        - **tags**: a set of unique tag strings for this item
    """
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}




items = {"foo": "The Foo Wrestlers"}


@error.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


@error.get("/items-header/{item_id}")
async def read_item(item_id: str):
    print('2' * 50)

    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found"
                            ,headers={"X-Error": "There goes my error", "X-Error2": "There goes my error"})
    return {"item": items[item_id]}