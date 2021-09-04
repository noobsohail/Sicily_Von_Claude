import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
STARTER_IMG = os.environ.get('STARTER_IMG', 'https://c.tenor.com/vIgfYyIueuoAAAAC/kenja-no-mago-sicily-von-claude.gif')
ANIME_NO_IMG = os.environ.get('ANIME_NO_IMG', 'https://media1.tenor.com/images/eaac56a1d02536ed416b5a080fdf73ba/tenor.gif?itemid=15075442')
ERRORS_CRY = os.environ.get('ERRORS_CRY', 'https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif' )
BOT_USERNAME = os.environ.get('BOT_USERNAME') #Input bot username without @ like ErzaScarlet_groupbot

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)