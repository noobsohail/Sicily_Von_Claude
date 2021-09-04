from Helper.helper import start_text, help_text
from config import bot, STARTER_IMG, BOT_USERNAME
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@{BOT_USERNAME}"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='{STARTER_IMG}'
        )

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help@{BOT_USERNAME}"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern="/source"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '[Source Code On Github](https://github.com/Nobbsohail/Sicily_von_Claude)\n Join [IndiAnime Disucssion Group](https://t.me/indianimein)'
        )
    
