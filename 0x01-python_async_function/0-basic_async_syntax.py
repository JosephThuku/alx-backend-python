#!/usr/bin/env python3
import asyncio
import random
"""0-basic_async_syntax.py"""


async def wait_random(max_delay=10):
    """await for a random seconds and the return it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
