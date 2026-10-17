from aiogram.fsm.state import StatesGroup, State


class TicketState(StatesGroup):
    waiting_category = State()
    waiting_message = State()