from aiogram import types, Dispatcher
from config import bot, GROUP_ID
from database.sql_commands import Database

async def ban_users_db(message: types.Message):
    db = Database()
    user = db.sql_select_ban_user(message.from_user.id)
    if user:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"Hey {user['username']}, you are in the ban table 😖. Your total violations: {user['count']}"
        )
    else:
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"Hey {message.from_user.username},you are not in the ban table 😉",
        )

def register_ban_users_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(ban_users_db,
                                        custom_filters=lambda call: call.data == "ban_users")