from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import TicketState

from database import (
    create_ticket,
    save_message
)

router = Router()


@router.message(TicketState.waiting_message)
async def receive_ticket(message: Message,
                         state: FSMContext):

    data = await state.get_data()

    ticket_id = create_ticket(
        message.from_user.id,
        data["category"]
    )

    save_message(
        ticket_id,
        "user",
        message.text or ""
    )

    await message.answer(
f"""
✅ <b>Обращение создано!</b>

🆔 Номер:

<b>#{ticket_id}</b>

📂 Категория:

<b>{data['category']}</b>

Наш оператор скоро вам ответит.
"""
    )

    await state.clear()