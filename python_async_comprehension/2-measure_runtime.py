#!/usr/bin/env python3
"""
Module to measure the runtime of executing async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time
from typing import Coroutine

# Import the async_comprehension coroutine from the previous file
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel.

    Uses asyncio.gather to run the coroutines concurrently and
    measures the total elapsed time.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()  # Start timer

    # Run four async_comprehension coroutines concurrently
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()  # End timer
    total_time = end_time - start_time

    return total_time
