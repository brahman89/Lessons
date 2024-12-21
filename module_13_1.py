import time
from time import sleep
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    i = 1
    while i != 6:
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i} шар.')
        i += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
