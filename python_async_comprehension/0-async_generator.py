#!/usr/bin/env python3
"""Module that defines an asynchronous generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields 10 random numbers.

    The coroutine loops 10 times, each time asynchronously waits
    for 1 second, then yields a random float between 0 and 10.

    Yields:
        float: random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
