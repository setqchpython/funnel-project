from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database import add_user
from keyboards import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    add_user(message.from_user)

    text = """
👋 <b>Добро пожаловать в поддержку Valkyrie VPN!</b>

Здесь вы можете:

🎫 Создать обращение

📂 Посмотреть свои обращения

❓ Получить ответы на популярные вопросы

──────────────────

🕒 Среднее время ответа:
<b>5–10 минут</b>
"""

    await message.answer(
        text,
        reply_markup=main_menu()
    )