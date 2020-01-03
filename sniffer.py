import asyncio, time, sys, signal


class ClientProtocol(asyncio.Protocol):
    def __init__(self, message, on_con_lost):
        self.message = message
        self.on_con_lost = on_con_lost

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print(str(data, "utf-8"))

    def connection_lost(self, exc):
        print('The server closed the connection')
        self.on_con_lost.set_result(True)

def signal_handler(sig, frame):
    print('\r\nEND of session')
    sys.exit(0)

async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.

#    loop = asyncio.get_running_loop()
#    loop = asyncio.get_event_loop()

    on_con_lost = loop.create_future()
    message = ('@\x15' '@MA' '@F0' '@Y0' '@h' '@l' '@\x16')

    transport, protocol = await loop.create_connection(
        lambda: ClientProtocol(message, on_con_lost),
        str(sys.argv[1]), 5045)

    try:
        await on_con_lost

    finally:
        transport.close()


if __name__ == "__main__":
    print ('Connect server ', str(sys.argv[1]))    
    signal.signal(signal.SIGINT, signal_handler)
    # asyncio.run(main())
    # If using Python 3.6 or below, use the following code instead of asyncio.run(main()):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
