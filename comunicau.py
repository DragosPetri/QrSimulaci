import websockets
import asyncio
import json
from qr import QR
import time
from door import simulate_door

path_to_image = "path.txt"


def handle(msg):
    if (msg == "open"):
        simulate_door()
    if (msg == "unauthorized"):
        f = open(path_to_image, "w")
        f.write("bad.png")
        f.close()
        time.sleep(3)
        f = open(path_to_image, "w")
        f.write("qr.png")
        f.close()


async def listen():
    url = "ws://financeapp.tudoresan.ro:8080/room/ws?id=6366b5b04483e1e9fbd14fc0"
    while (1):
        async with websockets.connect(url, ping_interval=None) as ws:

            while True:
                msg = await ws.recv()
                data = json.loads(msg)
                print(data)
                handle(data['message'])


asyncio.run(listen())
