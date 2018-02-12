import asyncio
async def long_task(x):
    print("Wait for 1/{:d} seconds...".format(x))
    await asyncio.sleep(1.0 / x)
    return 1.0 / x
coroutines = [long_task(i) for i in range(1, 101)]
loop = asyncio.get_event_loop()
all_futures = asyncio.gather(*coroutines)
loop.run_until_complete(all_futures)
loop.close()
