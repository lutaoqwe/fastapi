# 定义一个带路径参数的 GET 请求路由
import json
import time
import asyncio
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from openai import OpenAI
stream = APIRouter()


client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key= "sk-d2ef63b03e524bc99f72503beba6d48e",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

async def chat_stream_generator(question:str):
    """异步生成聊天流"""
    try:
        # 在生成器内部创建completion
        completion = client.chat.completions.create(
            model="qwen3-max-preview",
            stream=True,
            messages=[
                {"role": "system", "content": "你是一名Java技术专家，只为用户生成Java代码"},
                {"role": "user", "content": question},
            ],
        )

        # 流式返回每个chunk
        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                print(f"Yielding: {content}")
                yield f"data: {content}\n\n"
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        yield f"data: {json.dumps({'error': error_msg})}\n\n"


@stream.get("/rt")
async def stream_data(question:str):
    print("="  * 50)
    return StreamingResponse(
        chat_stream_generator(question),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )
