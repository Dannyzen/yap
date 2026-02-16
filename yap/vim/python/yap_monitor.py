import asyncio
import json
import uuid
import sys
import argparse

# Try to use websockets, but handle failure gracefully if not installed
try:
    import websockets
except ImportError:
    print("Error: 'websockets' module not found. Please install it with 'pip install websockets'", file=sys.stderr)
    sys.exit(1)

async def monitor(host, port, duration=None):
    uri = f"ws://{host}:{port}"
    uid = str(uuid.uuid4())
    
    try:
        async with websockets.connect(uri) as websocket:
            # 1. Handshake as a monitor (or just a passive client)
            # The server supports "monitor" role if we just don't send audio? 
            # Actually, looking at server.py, "monitor" is a specific role or we just listen.
            # The standard client sends a handshake.
            
            # Let's try to be a "monitor" if server supports it, or just a client that sends no audio.
            # Server.py has `handle_monitor_client` but it seems to be triggered by... what?
            # It seems `recv_audio` checks for options.
            
            # Handshake as a monitor
            handshake = {
                "uid": uid,
                "task": "monitor"
            }
            await websocket.send(json.dumps(handshake))
            
            # Wait for ready
            while True:
                resp = await websocket.recv()
                data = json.loads(resp)
                if data.get("status") == "MONITOR_READY":
                    break
            
            # Receive loop
            while True:
                try:
                    message = await websocket.recv()
                    data = json.loads(message)
                    
                    if "segments" in data:
                        for seg in data["segments"]:
                            if seg.get("completed"):
                                # Print finalized segments
                                print(f"{seg['text']}")
                                sys.stdout.flush()
                                
                except websockets.exceptions.ConnectionClosed:
                    break
                    
    except Exception as e:
        print(f"Connection error: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Yap Vim Monitor")
    parser.add_argument("--host", default="localhost", help="Server host")
    parser.add_argument("--port", type=int, default=9090, help="Server port")
    args = parser.parse_args()

    try:
        asyncio.run(monitor(args.host, args.port))
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
