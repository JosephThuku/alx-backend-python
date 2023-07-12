#!/usr/bin/env python3
"""
measure_runtime coroutine
This will execute async_comprehension four times
in parallel using asyncio.gather.
"""
import asyncio, random
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ measure the runtime """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
