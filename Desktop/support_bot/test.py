import asyncio
import aiohttp


async def main():
    url = "https://api.telegram.org"

    try:
        timeout = aiohttp.ClientTimeout(total=15)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url) as response:
                print("Status:", response.status)
                print(await response.text())

    except Exception as e:
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())