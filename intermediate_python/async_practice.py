import asyncio
import time
import aiohttp


# =====================================================
# 1. Basic async tasks
# =====================================================

async def hello(delay: int, msg: str) -> None:
    """Print message after a delay."""
    await asyncio.sleep(delay)
    print(msg)


async def demo_hello() -> None:
    """Run basic async task demo."""
    task1 = asyncio.create_task(hello(2, "from task T1"))
    task2 = asyncio.create_task(hello(1, "from task T2"))

    await task1
    await task2


# =====================================================
# 2. Async gather example
# =====================================================

async def task(name: str, delay: int) -> str:
    """Simulate async work and return result."""
    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} finished")
    return f"{name} result"


async def demo_gather() -> None:
    """Run asyncio.gather example."""
    start = time.time()

    results = await asyncio.gather(
        task("Task-1", 3),
        task("Task-2", 2),
        task("Task-3", 1),
    )

    print(results)
    print("Total Time:", round(time.time() - start, 2))


# =====================================================
# 3. Async worker + background task
# =====================================================

async def worker() -> None:
    """Simple async worker loop."""
    for i in range(5):
        print("Working...", i)
        await asyncio.sleep(1)


async def demo_worker() -> None:
    """Run worker with background task."""
    task = asyncio.create_task(worker())

    print("Task started")

    await asyncio.sleep(2)
    print("Doing other work")

    await task


# =====================================================
# 4. Async HTTP requests
# =====================================================

URLS = [
    "https://dummyjson.com/users/1",
    "https://dummyjson.com/users/2",
    "https://dummyjson.com/users/3",
    "https://dummyjson.com/users/4",
]


async def fetch(session: aiohttp.ClientSession, url: str) -> None:
    """Fetch user data from API."""
    async with session.get(url) as response:
        data = await response.json()
        print(data["firstName"])


async def demo_http() -> None:
    """Run async HTTP requests."""
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        await asyncio.gather(*tasks)

    print("Time:", round(time.time() - start, 2))


# =====================================================
# MAIN CONTROLLER
# =====================================================

async def main() -> None:
    """Run all async demos one by one."""
    print("\n===== HELLO DEMO =====")
    await demo_hello()

    print("\n===== GATHER DEMO =====")
    await demo_gather()

    print("\n===== WORKER DEMO =====")
    await demo_worker()

    print("\n===== HTTP DEMO =====")
    await demo_http()


if __name__ == "__main__":
    asyncio.run(main())