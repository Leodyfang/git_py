import asyncio


async def fake_io_operation():  # simulate some long I/O operations
    print("Perform I/O now...")
    await asyncio.sleep(1)
    print("I/O completed")


async def compute_square(x):
    print("Compute square of %d" % x)
    await fake_io_operation()
    print("Square of %d is %d" % (x, x * x))
    return x * x
# 1
# tasks = []
# for i in [4, 5, 6, 7]:
#     tasks.append(asyncio.ensure_future(compute_square(i)))
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
# 2
tasks = []
for i in [4, 5, 6, 7]:
    tasks.append(asyncio.ensure_future(compute_square(i)))
loop = asyncio.get_event_loop()
results, _ = loop.run_until_complete(
    asyncio.wait(tasks))
loop.close()
for f in results:
    print(f.result())
# 3
# coros = [compute_square(i) for i in range(5)]
# loop = asyncio.get_event_loop()
# all_futures = asyncio.gather(*coros)
# results = loop.run_until_complete(all_futures)
# loop.close()
# print (results)
# for f in results:
#     print(f)
