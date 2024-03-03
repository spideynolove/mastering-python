# python >= 3.10
import asyncio


async def echo():
    while True:
        received = await asyncio.to_thread(input, "Enter a value: ")
        sent = yield received
        print(f"Received: {sent}")


async def main():
    coroutine = echo()
    await coroutine.__anext__()  # Advance the coroutine to the first `yield`
    while True:
        value = await coroutine.asend(None)
        if value == 'exit':
            break

asyncio.run(main())