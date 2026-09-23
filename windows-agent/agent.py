import asyncio
import websockets

HOST = "0.0.0.0"
PORT = 8765


async def handle_client(websocket):
    print("Chromebook connected!")

    await websocket.send("WINDOWS_FOR_CHROMEBOOK_CONNECTED")

    try:
        async for message in websocket:
            print(f"Received: {message}")

            if message == "ping":
                await websocket.send("pong")

    except websockets.exceptions.ConnectionClosed:
        print("Chromebook disconnected.")


async def main():
    print("===================================")
    print(" Windows for Chromebook Agent")
    print("===================================")
    print(f"Listening on port {PORT}")
    print("Waiting for Chromebook...")

    async with websockets.serve(
        handle_client,
        HOST,
        PORT
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
