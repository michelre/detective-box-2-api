from fastapi import Request
import asyncio
import time

clients = {}


def create_client_queue(user_id):
    clients[user_id] = asyncio.Queue()


async def new_event(event, user_id):
    if user_id in clients:
        queue = clients[user_id]
        if queue:
            await queue.put(event)


async def get_event(user_id):
    queue = clients[user_id]
    return await queue.get()


async def event_generator(request: Request, user_id):
    while True:
        if await request.is_disconnected():
            delattr(clients, user_id)
            break

        yield await get_event(user_id)
