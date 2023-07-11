#!/usr/bin/python3
"""0-basic_async_syntax.py"""
import asyncio
import random


async def wait_random(max_delay=10):
    """await for a random seconds and the return it"""
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay
