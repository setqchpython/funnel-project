from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🎫 Создать обращение",
        callback_data="create_ticket"
    )

    kb.button(
        text="📂 Мои обращения",
        callback_data="my_tickets"
    )

    kb.button(
        text="❓ FAQ",
        callback_data="faq"
    )

    kb.button(
        text="🌐 Основной бот",
        url="https://t.me/USERNAME_BOT"
    )

    kb.adjust(1)

    return kb.as_markup()


def categories_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="🌐 VPN",
        callback_data="category_vpn"
    )

    kb.button(
        text="💳 Оплата",
        callback_data="category_payment"
    )

    kb.button(
        text="📱 Настройка",
        callback_data="category_setup"
    )

    kb.button(
        text="⚙️ Другое",
        callback_data="category_other"
    )

    kb.adjust(2)

    return kb.as_markup()


def cancel_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(
        text="❌ Отмена",
        callback_data="cancel_ticket"
    )

    return kb.as_markup()