import asyncio
import aiozmq.rpc


class ServerHandler(aiozmq.rpc.AttrHandler):

    @aiozmq.rpc.method
    def remote_func(self, a:int, b:int) -> int:
        print("in remote_func")
        return a + b


@asyncio.coroutine
def go():
    server = yield from aiozmq.rpc.serve_rpc(
        ServerHandler(), bind='tcp://127.0.0.1:5555')

    
def main():
    try:
        loop = asyncio.get_event_loop()
        asyncio.async(go())
        loop.run_forever()
    except KeyboardInterrupt:
        print()
        pass
    finally:
        print('step: loop.close()')
#        server.close()
#        server.wait_closed()
        loop.close()
    print("DONE")

if __name__ == '__main__':
    main()
