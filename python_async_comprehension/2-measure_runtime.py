#!/usr/bin/env python3
"""Measure runtime of 10 async_generator executions concurrently."""

import asyncio
import time
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def measure_runtime() -> float:
    """Run async_generator 10 times concurrently and measure runtime."""
    start = time.time()

    # Create 10 coroutines (one per async_generator call)
    coroutines: List[asyncio.Task] = [async_generator() for _ in range(10)]

    # Run them concurrently using gather
    results = await asyncio.gather(*coroutines)

    end = time.time()
    return end - start
