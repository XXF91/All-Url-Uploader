import os
import logging
from pyrogram.raw.all import layer
from pyrogram import Client, idle, __version__

from config import Config


bot = Client(
    "All-Url-Uploader",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    workers=50,
    plugins=dict(root="plugins"),
)

bot.start()
logger.info("Bot has started.")
logger.info("**Bot Started**\n\n**Pyrogram Version:** %s \n**Layer:** %s", __version__, layer)
logger.info("Developed by github.com/kalanakt Sponsored by www.netronk.com")
idle()
bot.stop()
logger.info("Bot Stopped ;)")
