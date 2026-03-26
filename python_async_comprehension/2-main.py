#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    """Run the measure_runtime coroutine and return its result."""
    return await measure_runtime()


print(asyncio.run(main()))
