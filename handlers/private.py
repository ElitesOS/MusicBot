import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/12514ab36b0869139b77a.jpg",
        caption=f"""**I Am A Smooth Telegram Music Bot With Fantastic Features & High Quality Songs**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "[Created By]", url=f"https://t.me/TeamB2k")
               ],
                [
                    InlineKeyboardButton(
                        "[Repository]", url=f"https://github.com/ElitesOS/MusicBot")
               ], 
                [
                    InlineKeyboardButton(
                        "[Support Chat]", url=f"https://t.me/TeamB2kSupport")
               ],
                [
                    InlineKeyboardButton(
                        "[Help] [24×7]", url=f"https://t.me/TeamB2kSupport")
                ]
                
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/12514ab36b0869139b77a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repository", url=f"https://github.com/ElitesOS/MusicBot")
                ]
            ]
        ),
    )
