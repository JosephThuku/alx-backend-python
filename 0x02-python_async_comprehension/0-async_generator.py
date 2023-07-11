#!/usr/bin/python3
"""" Async Generator """
import asyncio
import random


async def async_generator():
    """coroutine finction to iterate and yield """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)