import asyncio
import aiozmq.rpc
import msgpack
from . import common
from . import deck


class ServerHandler(aiozmq.rpc.AttrHandler):
    def __init__(self, clients):
        self.clients = clients

    @aiozmq.rpc.method
    def register(self, name, addr):
        self.clients.append((name, addr))
        

async def go(clients):
    handler = ServerHandler(clients)
    addr = 'ipc://%s' % common.server_socket
    server = await aiozmq.rpc.serve_rpc(handler, bind=addr)

    
class BlackJack(object):
    def __init__(self, clients, loop):
        self.clients = clients
        self.loop = loop
        self.deck = deck.Deck()
        self.current_hand = asyncio.Queue()


    async def run(self):
        print("in run")
        try:
            print("WAITING")
            while True:
                for name, addr in self.clients:
                    print("NEW HAND! %s" % name)
                    player_hand = [self.deck.draw(), self.deck.draw()]
                    dealer_hand = [self.deck.draw()]
#                    await self.current_hand.put(d)
                    conn = await aiozmq.rpc.connect_rpc(connect=addr)

                    action = None
                    while True:
                        d = dict(player=player_hand,
                                 dealer=dealer_hand)
                        action = await conn.call.action(d)
                        if action is 's':
                            break
                        player_hand += [self.deck.draw()]

                    while deck.calc_score(dealer_hand) <= 17:
                        dealer_hand += [self.deck.draw()]
                        d = dict(player=player_hand,
                                 dealer=dealer_hand)
                    await conn.call.complete(d)

                    conn.close()

                await asyncio.sleep(1)
        except Exception as e:
            print(e)

#    async def dist_hand(self):
#        print("in dist_hand")
#        try:
#            while True:
#                current_hand = await self.current_hand.get()
#                for name, addr in self.clients:
#                    conn = await aiozmq.rpc.connect_rpc(connect=addr)
#                    await conn.call.current_hand(current_hand)
#                    conn.close()
#                    print("blah")
#        except Exception as e:
#            print(e)

def main():
    clients = []
    try:
        loop = asyncio.get_event_loop()
        bj = BlackJack(clients, loop)
        loop.create_task(bj.run())
        asyncio.async(go(clients))
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
