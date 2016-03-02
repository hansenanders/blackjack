import asyncio
import aiozmq.rpc
from . import common
from . import deck

class ServerHandler(aiozmq.rpc.AttrHandler):
    @aiozmq.rpc.method
    def hello(self):
        print("HELLO WORLD")

    @aiozmq.rpc.method
    def action(self, hand):
        deck.print_hand(hand)
        action = input("h (Hit), s (Stand): ")
        return action

    @aiozmq.rpc.method
    def complete(self, hand):
        print("----------")
        deck.print_hand(hand)
        print("----------")

@asyncio.coroutine
async def go():
    handler = ServerHandler()
    name = "client1"
    server_addr = 'ipc://%s/%s' % (common.base_path, name)
    server = await aiozmq.rpc.serve_rpc(handler, bind=server_addr)

    client = await aiozmq.rpc.connect_rpc(
        connect='ipc://%s' % common.server_socket)
    await client.call.register(name, server_addr)
    client.close()

    
try:
    loop = asyncio.get_event_loop()
    asyncio.async(go())
    loop.run_forever()
except KeyboardInterrupt:
    print()
    pass
finally:
    print('step: loop.close()')
    loop.close()
