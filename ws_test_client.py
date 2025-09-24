import asyncio
import websockets

async def test_websocket():
    uri = "ws://localhost:5000"
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server")
        await websocket.send("Hello server!")
        response = await websocket.recv()
        print(f"Received from server: {response}")

if __name__ == "__main__":
    asyncio.run(test_websocket())
