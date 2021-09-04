from telethon import events
import Helper.formating_results as format
from API.nhentaiapi import nhentaiapi as hentai
from config import bot, ANIME_NO_IMG, BOT_USERNAME

class Nhentai():

    @bot.on(events.NewMessage(pattern="/hentai"))
    async def event_handler_anime(event):
        if '/hentai' == event.raw_text:
            await bot.send_message(
                event.chat_id,
                'Command must be used like this\n/hentai <hentai code\nexample: /hentai 339989',
                file=f'{ANIME_NO_IMG}'
            )
        elif '/hentai' in event.raw_text:
            text = event.raw_text.split()
            text.pop(0)
            code = " ".join(text)
            chapter = hentai.get_chapter_by_code(code)
            format.manga_chapter_html(f"{code}", chapter)
            await bot.send_message(
                event.chat_id,
                "Open this in google chrome",
                file= f"{code}.html"
            )
