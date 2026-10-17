from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import (
    categories_keyboard,
    main_menu
)

from states import TicketState

router = Router()


@router.callback_query(lambda c: c.data == "create_ticket")
async def create_ticket(callback: CallbackQuery,
                        state: FSMContext):

    await callback.message.edit_text(

        "📂 Выберите категорию обращения.",

        reply_markup=categories_keyboard()

    )

    await state.set_state(
        TicketState.waiting_category
    )

    await callback.answer()


@router.callback_query(lambda c: c.data.startswith("category_"))
async def category(callback: CallbackQuery,
                   state: FSMContext):

    category = callback.data.split("_")[1]

    names = {
        "vpn": "VPN",
        "payment": "Оплата",
        "setup": "Настройка",
        "other": "Другое"
    }

    await state.update_data(
        category=names[category]
    )

    await callback.message.edit_text(
        f"""
<b>Категория:</b> {names[category]}

Теперь подробно опишите проблему.

Можно прикрепить:

📷 Фото

📄 Документ

🎥 Видео

🎤 Голосовое сообщение
"""
    )

    await state.set_state(
        TicketState.waiting_message
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "faq")
async def faq(callback: CallbackQuery):

    await callback.message.edit_text(
"""
❓ <b>FAQ</b>

• Как установить VPN?

• Как купить подписку?

• Где взять конфигурацию?

• VPN не работает.

Нажмите /start чтобы вернуться.
"""
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "my_tickets")
async def my_tickets(callback: CallbackQuery):

    await callback.answer(
        "Пока у вас нет обращений.",
        show_alert=True
    )