# middleware/process_time.py
import time
from fastapi import Request


async def add_process_time_header(request: Request, call_next):
    """
    处理时间中间件
    """
    print('执行前' * 10)

    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = f"{process_time:.4f}s"
    print('执行后' * 10)

    return response