from datetime import timedelta, datetime
from aiogram import types, Dispatcher
from config import bot, GROUP_ID
from profanity_check import predict, predict_prob

from database.sql_commands import Database


async def chat_messages(message: types.Message):
    db = Database()
    if message.chat.id == int(GROUP_ID):
        ban_word_predict_prob = predict_prob([message.text])
        print(ban_word_predict_prob)
        if ban_word_predict_prob[0] > 0.5:
            user = db.sql_select_ban_user(
                tg_id=message.from_user.id
            )
            print(user)
            if not user:
                db.sql_insert_new_ban_user(
                    tg_id=message.from_user.id
                )
            elif user['count'] >= 3:
                await message.delete()
                await bot.send_photo(
                    chat_id=message.chat.id,
                    photo=open("MEDIA_DESTINATION/red.jpg", "rb"),
                    caption="You are banned ❌",
                    reply_markup=types.ReplyKeyboardRemove(),
                )
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    until_date=datetime.now() + timedelta(minutes=2)
                )
            else:
                db.sql_update_ban_user_count(
                    tg_id=message.from_user.id
                )

            await message.delete()
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=open("MEDIA_DESTINATION/yellow.jpg", "rb"),
                caption=f"You used a bad word\n"
                        f"you get a yellow card {message.from_user.first_name}\n"
                        f"The third time you will receive a red card and you will be banned",
                reply_markup=types.ReplyKeyboardRemove(),
            )



def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)