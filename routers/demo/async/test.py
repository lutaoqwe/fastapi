
import asyncio

import time

from routers.demo.enums import ModelName


# 模拟一个“慢任务”——点外卖需要 3 秒
async def order_food(food: str):
    print(f"开始点 {food}...")
    await asyncio.sleep(3)  # 模拟等待送餐
    print(f"{food} 已经送到了！")
    return food


async def main():
    start = time.time()
    task1 = asyncio.create_task(order_food("汉堡"))
    task2 = asyncio.create_task(order_food("Cole"))

    print("下单完成，休息一会")

    food1 = await task1
    food2 = await task2
    print(f"吃到 {food1} 和 {food2} 了！")
    end = time.time()
    print(f"总共花费 {end - start:.2f} 秒")

    print(ModelName.alexnet.value)






if __name__ == '__main__':
    asyncio.run(main())

#burgers = await get_burgers(2)
#print(burgers)
