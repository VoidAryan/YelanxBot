from Yelan import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/fa2c031ecf5df678280e5.jpg"

def alive(update: Update, context: CallbackContext):
    TEXT = f"ɪ ᴀᴍ ʏᴇʟᴀɴ ᴀᴋᴀ ʜᴇᴀᴅ ᴏꜰ ʏᴀɴꜱʜᴀɴ ᴛᴇᴀʜᴏᴜꜱᴇ 🥀\n\nI ɢᴀɴɢᴇᴅ ᴜᴘ ᴡɪᴛʜ 🔥 : **[【V๏ɪ፝֟𝔡】 ✧Network✧](https://t.me/voidxnetwork)** \n\nᴡᴀɴᴛ ᴀ ʜᴏᴛ ʙᴏᴛ ᴛᴏ ꜰʟᴀᴛᴛᴇʀ ᴍᴇᴍʙᴇʀꜱ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ? ɪ ᴀᴍ ʜᴇʀᴇ ✨🤞"
    

    update.effective_message.reply_photo(
        PHOTO, caption= TEXT,
        parse_mode=ParseMode.MARKDOWN,

            reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="【Support】", url="https://t.me/yelanxsupport"),
                InlineKeyboardButton(text="【Updates】", url="https://t.me/yelanxupdates")
                ],
                [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/voidxnetwork")]
            ]
        ),
    )

void_handler = CommandHandler("alive", alive, run_async = True)
dispatcher.add_handler(void_handler)


__help__ = """ 
❂ /alive: To check if bot is alive or not."""
   
__mod_name__ = "Alive"
