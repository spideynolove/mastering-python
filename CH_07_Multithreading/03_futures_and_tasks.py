import asyncio


async def sleeper(delay):
    await asyncio.sleep(delay)
    print('Finished sleeper with delay: %.1f' % delay)


async def stack_printer():
    for task in asyncio.Task.all_tasks():
        # print(type(task))
        task.print_stack()


if __name__ == "__main__":
    '''
    # Create an event loop
    loop = asyncio.get_event_loop()

    # Create the task
    result = loop.call_soon(loop.create_task, sleeper(0.2))
    # loop.run_forever()``

    # Make sure the loop stops after 1.2 seconds
    result = loop.call_later(1.2, loop.stop)

    loop.run_forever()
    '''

    # for debugging purposes
    # Create an event loop
    loop = asyncio.get_event_loop()

    # Create the task
    result = loop.run_until_complete(stack_printer())