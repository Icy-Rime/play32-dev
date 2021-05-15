import asyncio

# Core functions
create_task = asyncio.create_task
current_task = asyncio.current_task
run = asyncio.run
sleep = asyncio.sleep
async def sleep_ms(t):
    await asyncio.sleep(t / 1000)

# Additional functions
wait_for = asyncio.wait_for
async def wait_for_ms(awaitable, timeout):
    return await asyncio.wait_for(awaitable, timeout / 1000)
gather = asyncio.gather

# class Task
Task = asyncio.Task

# class Event
Event = asyncio.Event

# class ThreadSafeFlag
class ThreadSafeFlag():
    def __init__(self):
        self.__flag = False
    def set(self):
        self.__flag = True
    async def wait(self):
        while not self.__flag:
            await asyncio.sleep(0.0)

# class Lock
Lock = asyncio.Lock

# TCP stream connections
open_connection = asyncio.open_connection
start_server = asyncio.start_server
# Stream = asyncio.StreamWriter
# Server = asyncio.AbstractServer

# Event Loop
get_event_loop = asyncio.get_event_loop
new_event_loop = asyncio.new_event_loop
Loop = asyncio.BaseEventLoop
