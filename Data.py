from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("โ Start Generating Session โ", callback_data="generate")],
        [InlineKeyboardButton(text=" Back ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("๐ฅ Start Generating Session ๐ฅ", callback_data="generate")]
    ]

    support_button = [
        [InlineKeyboardButton("โ Support โ", url="https://t.me/tigernetwork"")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("๐ฅ Start Generating Session ๐ฅ", callback_data="generate")],
        [InlineKeyboardButton("๐จโ๐ป Network ๐จโ๐ป", url="https://t.me/tigernetwork")],
        [
            InlineKeyboardButton("How to Use โ", callback_data="help"),
            InlineKeyboardButton(" About", callback_data="about")
        ],
        [InlineKeyboardButton("๐ฎ๐ณ Owner ๐ฎ๐ณ", url="https://t.me/tigernetwork")],
    ]

    # Help Message
    HELP = """
ยป Click the below button or use /generate command to start generating session!
ยป Click the required button; [Pyrogram/Telethon]
ยป Enter the required variables when asked.
"""

    # About Message
    ABOUT = """
๐จโ๐ป **About Me** 

A telegram bot to generate pyrogram and telethon string session...

[Pyrogram](docs.pyrogram.org)
[Telethon](docs.telethon.org)

Language : [Python](www.python.org)
            **Regarding ~ **@thefather69
"""
