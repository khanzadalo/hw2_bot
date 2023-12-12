from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_buttons
from keyboards.inline_buttons import new_movie_keyboard,movie_snack_keyboard


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="What is your favorite movie genre?🎥",
        reply_markup=await inline_buttons.start_questionnaire_keyboard()
    )


async def comedy_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh cool, I like to laugh too 😆",
        reply_markup=await new_movie_keyboard()
    )


async def drama_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh, and you are a lover of crying 😅",
        reply_markup=await new_movie_keyboard()
    )


async def fantasy_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="An excellent choice!🔮",
        reply_markup=await new_movie_keyboard()
    )


async def action_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Oh yeah the action movies are the best!💪",
        reply_markup=await new_movie_keyboard()
    )


async def romance_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Ah, romance 💘",
        reply_markup=await new_movie_keyboard()
    )


async def other_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Very curious 🧐",
        reply_markup=await new_movie_keyboard()
    )




async def start_watch_movie_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Who would you rather watch movies with? 🍿👥",
        reply_markup=await inline_buttons.start_watch_movie_keyboard()
    )


async def friends_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Watching movies with friends is always fun! 👫👭👬",
        reply_markup=await watch_movie_keyboard()
    )


async def family_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Enjoying movies with family creates special moments! 👪",
        reply_markup=await watch_movie_keyboard()
    )


async def alone_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Sometimes it's nice to watch movies alone and have some personal time! 🚶‍♂️📺",
        reply_markup=await watch_movie_keyboard()
    )


async def partner_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Snuggling up and watching movies with your partner is so cozy! ❤️🍿",
        reply_markup=await watch_movie_keyboard()
    )


async def start_new_movie_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="What do you prefer to watch the movie on? 🎥📺",
        reply_markup=await inline_buttons.start_new_movie_keyboard()

    )


async def cinema_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Watching movies in the cinema gives you a big screen and immersive experience! 🍿🎬",
        reply_markup=await movie_snack_keyboard()
    )


async def tv_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="A TV provides a great viewing experience for movies! 📺🍿",
        reply_markup=await movie_snack_keyboard()
    )


async def online_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Watching movies on a mobile device or laptop gives you flexibility on-the-go! 📱💻",
        reply_markup=await movie_snack_keyboard()
    )

async def start_movie_snack_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="What is your favorite kind of movie snack? 🍿",
        reply_markup=await inline_buttons.start_movie_snack_keyboard()
    )


async def popcorn_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Nice choice! Popcorn is a classic movie snack! 🍿\n"
             "Thank you for taking my mini survey,bye 👋"
    )


async def chips_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Crunchy chips are always a great movie snack! 🍟\n"
             "Thank you for taking my mini survey,bye 👋"
    )


async def chocolate_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Yum! Chocolate is a delicious movie treat! 🍫\n"
             "Thank you for taking my mini survey,bye 👋"
    )


async def fruits_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Healthy choice! Fruits are a refreshing snack while watching movies! 🍎\n"
             "Thank you for taking my mini survey,bye 👋"
    )


async def other_snack_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Interesting! There are so many other options for movie snacks! 🍉\n"
             "Thank you for taking my mini survey,bye 👋"
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(comedy_call,
                                       lambda call: call.data == "comedy")
    dp.register_callback_query_handler(drama_call,
                                       lambda call: call.data == "drama")
    dp.register_callback_query_handler(fantasy_call,
                                       lambda call: call.data == "fantasy")
    dp.register_callback_query_handler(action_call,
                                       lambda call: call.data == "action")
    dp.register_callback_query_handler(romance_call,
                                       lambda call: call.data == "romance")
    dp.register_callback_query_handler(other_call,
                                       lambda call: call.data == "other")

    dp.register_callback_query_handler(start_movie_snack_call,
                                       lambda call: call.data == "movie_snack")
    dp.register_callback_query_handler(popcorn_call,
                                       lambda call: call.data == "popcorn")
    dp.register_callback_query_handler(chips_call,
                                       lambda call: call.data == "chips")
    dp.register_callback_query_handler(chocolate_call,
                                       lambda call: call.data == "chocolate")
    dp.register_callback_query_handler(fruits_call,
                                       lambda call: call.data == "fruits")
    dp.register_callback_query_handler(other_snack_call,
                                       lambda call: call.data == "other")

    dp.register_callback_query_handler(start_watch_movie_call,
                                       lambda call: call.data == "watch_movie")
    dp.register_callback_query_handler(friends_call,
                                       lambda call: call.data == "friends")
    dp.register_callback_query_handler(family_call,
                                       lambda call: call.data == "family")
    dp.register_callback_query_handler(partner_call,
                                       lambda call: call.data == "partner")
    dp.register_callback_query_handler(alone_call,
                                       lambda call: call.data == "alone")

    dp.register_callback_query_handler(start_new_movie_call,
                                       lambda call: call.data == "new_movie")
    dp.register_callback_query_handler(cinema_call,
                                       lambda call: call.data == "cinema")
    dp.register_callback_query_handler(tv_call,
                                       lambda call: call.data == "tv")
    dp.register_callback_query_handler(online_call,
                                       lambda call: call.data == "online")
