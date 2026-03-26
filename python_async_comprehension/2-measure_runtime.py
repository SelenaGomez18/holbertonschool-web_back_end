#!/usr/bin/env python3
"""
Module defining an asynchronous generator that produces 10 random numbers
between 0 and 10, waiting 1 second between each generation.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Generate 10 random numbers asynchronously, one per second.

    This asynchronous generator loops 10 times, waits 1 second
    in each iteration, and yields a random float between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
