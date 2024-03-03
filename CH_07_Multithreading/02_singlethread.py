import asyncio


async def sleeper(delay):
    await asyncio.sleep(delay)
    print('Finished sleeper with delay: %.1f' % delay)

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.wait((
    sleeper(0.3),
    sleeper(0.5),
    sleeper(0.8),
    sleeper(1.3),
)))