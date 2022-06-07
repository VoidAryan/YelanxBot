"""
import time
import os
import asyncio
import pyrogram

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.errors import UserNotParticipant
from Yelan.modules.renamer.scrimp import scrimp
from Yelan.modules.renamer.rerewurmk import rename_as_doc, rename_as_video
from Yelan import pbot




@pbot.on_message(filters.command["rename", "rename@YorForger_Bot"],filters.private & (filters.document | filters.video))
async def rename_cb(bot, update):
 
    file = update.document or update.video
    try:
        filename = file.file_name
    except:
        filename = "Not Available"
    
    await bot.send_message(
        chat_id=update.chat.id,
        text="<b>File Name</b> : <code>{}</code> \n\nSelect the desired option below 😇".format(filename),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Rename as Video", callback_data="rename_vid")],
                                                [InlineKeyboardButton(text="Rename as Doc", callback_data="rename_doc")],
                                                [InlineKeyboardButton(text="✖️ CANCEL ✖️", callback_data="cancel_e")]]),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True   
    )   


async def cancel_extract(bot, update):
    
    await bot.send_message(
        chat_id=update.chat.id,
        text="Process Cancelled 🙃",
    )

@pbot.on_callback_query()
async def cb_handler(bot, update):
        
    if "rename_vid" in update.data:
        query = update.message.replace("/rename", "")
        await update.message.delete()
        await rename_as_video(bot, query)
        
    elif "rename_doc" in update.data:
        query = update.message.replace("/rename", "")
        await update.message.delete()
        await rename_as_doc(bot, update.message)
        
    elif "cancel_e" in update.data:
        await update.message.delete()
        await cancel_extract(bot, update.message)

"""
