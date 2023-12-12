from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🔥",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup

async def start_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    comedy_button = InlineKeyboardButton(
        "Comedy 🤣",
        callback_data="comedy"
    )
    drama_button = InlineKeyboardButton(
        "Drama 😭",
        callback_data="drama"
    )
    fantasy_button = InlineKeyboardButton(
        "Fantasy 🧚‍♀️",
        callback_data="fantasy"
    )
    action_button = InlineKeyboardButton(
        "Action 🤼‍♂️",
        callback_data="action"
    )
    romance_button = InlineKeyboardButton(
        "Romance 💑",
        callback_data="romance"
    )
    other_button = InlineKeyboardButton(
        "Other 🙃",
        callback_data="other"
    )

    markup.add(comedy_button)
    markup.add(drama_button)
    markup.add(fantasy_button)
    markup.add(action_button)
    markup.add(romance_button)
    markup.add(other_button)
    return markup

async def new_movie_keyboard():
    markup = InlineKeyboardMarkup()
    new_movie_button = InlineKeyboardButton(
        "New Movie 🎥",
        callback_data="new_movie"
    )
    markup.add(new_movie_button)
    return markup


async def start_new_movie_keyboard():
    markup = InlineKeyboardMarkup()
    cinema_button = InlineKeyboardButton(
        "Watch a movie at the cinema 🍿",
        callback_data="cinema"
    )
    tv_button = InlineKeyboardButton(
        "Watch a movie on TV 📺",
        callback_data="tv"
    )
    online_button = InlineKeyboardButton(
        "Watch a movie online 💻",
        callback_data="online"
    )
    markup.add(cinema_button)
    markup.add(tv_button)
    markup.add(online_button)

    return markup


async def watch_movie_keyboard():
    markup =InlineKeyboardMarkup()
    watch_movie_button = InlineKeyboardButton(
        "Watch Movie 🍿",
        callback_data="watch_movie"
    )
    markup.add(watch_movie_button)
    return markup


async def start_watch_movie_keyboard():
    markup = InlineKeyboardMarkup()
    alone_button = InlineKeyboardButton(
        "Watch a movie alone 🙍‍♂️",
        callback_data="alone"
    )
    friends_button = InlineKeyboardButton(
        "Watch a movie with friends 👬👨🏽‍🤝‍👨🏻",
        callback_data="friends"
    )
    family_button = InlineKeyboardButton(
        "Watch a movie with your family 👨‍👩‍👧‍👦",
        callback_data="family"
    )
    partner_button = InlineKeyboardButton(
        "Watch a movie with your partner 💏"
    )
    markup.add(alone_button)
    markup.add(friends_button)
    markup.add(family_button)
    markup.add(partner_button)

    return markup


async def movie_snack_keyboard():
    markup = InlineKeyboardMarkup()
    movie_snack_button = InlineKeyboardButton(
        "Movie Snack 🍫",
        callback_data="movie_snack"
    )
    markup.add(movie_snack_button)
    return markup


async def start_movie_snack_keyboard():
    markup = InlineKeyboardMarkup()
    popcorn_button = InlineKeyboardButton(
        "Popcorn 🍿",
        callback_data = "popcorn"
    )
    chips_button = InlineKeyboardButton(
        "Chips 🍠",
        callback_data="chips"
    )
    chocolate_button = InlineKeyboardButton(
        "Chocolate 🍫",
        callback_data="chocolate"
    )
    fruits_button = InlineKeyboardButton(
        "Fruits 🍎",
        callback_data="fruits"
    )
    other_button = InlineKeyboardButton(
        "Other 🍉",
        callback_data="other"
    )
    markup.add(popcorn_button)
    markup.add(chips_button)
    markup.add(chocolate_button)
    markup.add(fruits_button)
    markup.add(other_button)

    return markup
