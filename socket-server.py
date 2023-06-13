import asyncio
import websockets
import redis

async def handler(websocket):
    redis_con = redis.Redis(host='localhost')
    
    pubsub = redis_con.pubsub()
    pubsub.subscribe('user_id_1') # 引数にする必要ある
    
    for listen_result in pubsub.listen():
        if listen_result['type'] == 'message': # pushされたらこういう結果が来る　{'type': 'message', 'pattern': None, 'channel': b'user_id_1', 'data': b'hello'}
            await websocket.send(listen_result['data'].decode('utf-8'))

    
async def main():
    async with websockets.serve(handler, "localhost", 6789):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

