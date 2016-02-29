import asyncio
import aiozmq.rpc

@asyncio.coroutine
def go():
    print("in go")
    client = yield from aiozmq.rpc.connect_rpc(
        connect='tcp://127.0.0.1:5555')
    ret = yield from client.call.remote_func(1, 2)
    client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()
