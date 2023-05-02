import asyncio


async def one():
    print("Doing 'one'...")
    await asyncio.sleep(1)
    print("End of 'one'!")


async def main():
    await one()


asyncio.run(main())