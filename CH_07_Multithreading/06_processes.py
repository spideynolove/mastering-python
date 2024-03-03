import time
'''
import subprocess
t = time.time()


def process_sleeper():
    print('Started sleep at %.1f' % (time.time() - t))
    process = subprocess.Popen(['sleep', '0.3'])
    process.wait()
    print('Finished sleep at %.1f' % (time.time() - t))


for i in range(3):
    process_sleeper()
# '''
# ------------------------------------------------------------------------------
'''
import subprocess


t = time.time()


def process_sleeper():
    print('Started sleep at %.1f' % (time.time() - t))
    return subprocess.Popen(['sleep', '0.3'])

processes = []
for i in range(5):
    processes.append(process_sleeper())

for process in processes:
    returncode = process.wait()
    print('Finished sleep at %.1f' % (time.time() - t))

# '''

# ------------------------------------------------------------------------------
# '''
import asyncio
t = time.time()


async def async_process_sleeper():
    print('Started sleep at %.1f' % (time.time() - t))
    process = await asyncio.create_subprocess_exec('sleep', '0.3')
    await process.wait()
    print('Finished sleep at %.1f' % (time.time() - t))


loop = asyncio.get_event_loop()
for i in range(5):
    task = loop.create_task(async_process_sleeper())

future = loop.call_later(1.5, loop.stop)

loop.run_forever()


# ------------------------------------------------------------------------------
# async def show_sleeper():
#     for _ in range(5):
#         await async_process_sleeper()


# async def main():
#     tasks = [async_process_sleeper() for i in range(5)]
#     await asyncio.gather(*tasks)

#     # # using asyncio.create_task
#     # tasks = asyncio.create_task(show_sleeper())
#     # await tasks

# asyncio.run(main())
# '''