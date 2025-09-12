from fastapi import FastAPI


from routers.user.url import user
from routers.shop.url import shop
from routers.stream.url import stream

app = FastAPI()


app.include_router(user, prefix="/user", tags=["用户"])
app.include_router(shop, prefix="/shop", tags=["购物"])
app.include_router(stream, prefix="/stream", tags=["streaming return"])


# 启动应用（用于直接运行）
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)