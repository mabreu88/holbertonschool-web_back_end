#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """integer argument (max_delay, with a default value of 10)
    named wait_random"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
