from CraftiGames import *
import asyncio


async def main():
    async with Pikanetwork() as api:

        for k in range(1000):
            try:
                await api.Profile("Fireor")
                print('success')
            except APIBlockedException:
                print('fail')

async def main2():
    await asyncio.gather(*[main() for k in range(100)])

if __name__ == '__main__':
    asyncio.run(main2())