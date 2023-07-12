#!/usr/bin/env python3
""" async comprehension """
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    random_numbers = [number async for number in async_generator()]
    return random_numbers
