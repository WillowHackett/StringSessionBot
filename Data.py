from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

We are warmly welcome to {} you can generate pyrogram String Session and enjoy

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram string session. Use below buttons to learn more !

By @mrkpbots with love
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/mrkpbots/4")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/mrkpbots")],
    ]

    # Help Message
    HELP = """
Just Follow Steps one by one for string session generate you must have API ID and API HASH 

If you don't have please make new from telegram website https://my.telegram.org/

✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram string session by @StarkBots

Source Code : [Click Here](https://youtube.com/channel/UCKcntT2R8QNJaRwhnQIgRfA)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : [MRKP BOTS](https://t.me/mrkpbots)
    """
