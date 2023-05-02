import asyncio


async def one():
    print("Doing 'one'...")
    print("We pause in 'one'...")
    await asyncio.sleep(1)
    print("Explicit context switch to 'one' again")
    print("End of 'one'!")


async def two():
    print("    Doing 'two'...")
    print("    We pause in 'two'...")
    await asyncio.sleep(1)
    print("    Implicit context switch back to 'two'")
    print("    End of 'two'!")


async def main():
    tasks = [one(), two()]
    await asyncio.gather(*tasks)


asyncio.run(main())
