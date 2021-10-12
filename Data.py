from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can force your group's users to join a particular chat.\n
The chat can be a group or channel. It can be private or public.

Click on How to Use Me Button to learn more !

Made With 💕 By @Tellybots_4u
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏡 Return Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🤖 Update Channel", url="https://t.me/tellybots_4u")],
        [
            InlineKeyboardButton("How to Use me ❔", callback_data="help"),
            InlineKeyboardButton("👲 About", callback_data="about")
        ],
        [InlineKeyboardButton("💬 Support Group", url="https://t.me/tellybots_support")],
        [InlineKeyboardButton("🚦 Bot Status", url="https://t.me/tellybots_support")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001505616678` or `/forcesubscribe -1001375849192`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

 **Available Commands** 

/fsub - See current force subscribe chat
/fsub chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

**Note** - You can also use `/forcesubscribe` instead of `/fsub`
    """

    # About Message
    ABOUT = """
**About Me** 

👲 Maintained by : [Tellybots4u](https://t.me/Tellybots_4u)

⚗️ Source Code : [Click Here](https://t.me/tellybots_digital)

🗃️ Framework : [Pyrogram](docs.pyrogram.org)

📚 Language : [Python](www.python.org)

🧒 Developer : @Tellybots_4u
    """
