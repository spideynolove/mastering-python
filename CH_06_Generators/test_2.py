import asyncio


async def producer(queue):
    for i in range(1, 6):
        await asyncio.sleep(0.5)  # Simulate slow production
        await queue.put(f"Item {i}")


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")  # f"Item {i}"
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await asyncio.sleep(3)  # Let the producer work for a while
    await queue.join()  # Wait for all items to be consumed
    await queue.put(None)  # Signal the consumer to exit

    # Wait for tasks to finish
    await asyncio.gather(producer_task, consumer_task)

asyncio.run(main())