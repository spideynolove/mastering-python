'''
# loop won't allow running of coroutines directly.
import time
import asyncio


t = time.time()

def printer(name):
    print('Started %s at %.1f' % (name, time.time() - t))
    time.sleep(0.2)
    print('Finished %s at %.1f' % (name, time.time() - t) + '\n-----------------------------\n')


loop = asyncio.get_event_loop()
result = loop.call_at(loop.time() + .2, printer, '\ncall_at\n-------------\n')
result = loop.call_later(.1, printer, '\ncall_later\n-------------\n')
result = loop.call_soon(printer, '\ncall_soon\n-------------\n')
result = loop.call_soon_threadsafe(printer, '\ncall_soon_threadsafe\n-------------\n')

# Make sure we stop after a second
result = loop.call_later(2, loop.stop)

loop.run_forever()
# ------------------------------------------------------------------------------
'''
# loop.create_task internally to wrap the coroutine
import time
import asyncio


t = time.time()

async def printer(name):
    print('Started %s at %.1f' % (name, time.time() - t))
    await asyncio.sleep(0.2)
    print('Finished %s at %.1f' % (name, time.time() - t))


loop = asyncio.get_event_loop()

result = loop.call_at(loop.time() + .2, loop.create_task, printer('call_at'))
result = loop.call_later(.1, loop.create_task, printer('call_later'))
result = loop.call_soon(loop.create_task, printer('call_soon'))
result = loop.call_soon_threadsafe(loop.create_task, printer('call_soon_threadsafe'))

# Make sure we stop after a second
result = loop.call_later(1, loop.stop)

loop.run_forever()
# '''