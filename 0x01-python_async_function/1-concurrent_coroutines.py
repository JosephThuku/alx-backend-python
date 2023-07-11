#!/usr/bin/env python3
import asyncio
import random
from typing import List
from heapq import nsmallest
wait_random = __import__('0-basic_async_syntax').wait_random
"""0-basic_async_syntax.py"""


async def wait_n(n: int = 0, max_delay: int = 10) -> list:
    """ spawn the function n times """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return nsmallest(n, delays)
