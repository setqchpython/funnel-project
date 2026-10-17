import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from database import create_tables

from handlers.start import router as start_router
from handlers.callbacks import router as callback_router
from handlers.user import router as user_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


async def main():

    create_tables()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(callback_router)
    dp.include_router(user_router)

    print("Бот запущен.")

    try:
        await dp.start_polling(bot)
    except Exception as e:
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())