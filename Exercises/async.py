# # import asyncio

# # async def hello(delay,msg):
# #     await asyncio.sleep(delay)
# #     print(msg)


# # async def main():
# #     t1=asyncio.create_task(hello(2,"from task T1"))
# #     t2=asyncio.create_task(hello(1,"from task T2"))
    
# #     await t1
# #     await t2
    
# # asyncio.run(main())


# import asyncio
# import time


# async def task(name, delay):

#     print(f"{name} started")

#     await asyncio.sleep(delay)

#     print(f"{name} finished")

#     return f"{name} result"


# async def main():

#     start = time.time()

#     results = await asyncio.gather(
#         task("Task-1", 3),
#         task("Task-2", 2),
#         task("Task-3", 1)
#     )

#     print(results)

#     print("Total Time:", time.time() - start)


# asyncio.run(main())
    
    

    
import asyncio


# async def worker():

#     for i in range(5):

#         print("Working...", i)

#         await asyncio.sleep(1)


# async def main():

#     task = asyncio.create_task(worker())

#     print("Task started")

#     await asyncio.sleep(2)

#     print("Doing other work")

#     await task


# asyncio.run(main())



import asyncio
import aiohttp
import time



urls = [
    "https://dummyjson.com/users/1",
    "https://dummyjson.com/users/2",
    "https://dummyjson.com/users/3",
    "https://dummyjson.com/users/4"
]


async def fetch(session, url):

    async with session.get(url) as response:

        data = await response.json()

        print(data["firstName"])


async def main():

    start = time.time()

    async with aiohttp.ClientSession() as session:

        tasks = [
            fetch(session, url)
            for url in urls
        ]

        await asyncio.gather(*tasks)

    print("Time:", time.time() - start)


asyncio.run(main())