import asyncio


async def exps_of_number(nb):
    limit = 10
    res = []

    n = 1
    while n < limit:
        print(nb ** n)
        n = n + 1
    print("---")


async def main():
    tasks = [exps_of_number(3), exps_of_number(5), exps_of_number(8)]
    await asyncio.gather(*tasks)


asyncio.run(main())
