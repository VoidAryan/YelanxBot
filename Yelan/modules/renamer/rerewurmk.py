import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import os
import time
import asyncio
import pyrogram


from YorForger.modules.renamer.scrimp import scrimp

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

from YorForger.modules.renamer.rehelp import progress_for_pyrogram

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from PIL import Image

    
async def rename_as_doc(bot, message):
    
    mssg = await bot.get_messages(
        message.chat.id,
        message.reply_to_message.message_id
    )    
    
    media = mssg.reply_to_message

    
    if media.empty:
        await message.reply_text('Why did you delete that 😕', True)
        return
        
    filetype = media.video or media.document
    try:
        actualname = filetype.file_name
        splitit = actualname.split(".")
        extension = (splitit[-1])
    except:
        extension = "mkv"

    await bot.delete_messages(
        chat_id=message.chat.id,
        message_ids=message.reply_to_message.message_id,
        revoke=True
    )
    
        file_name = message.text
        description = scrimp.CUSTOM_CAPTION_UL_FILE.format(newname=file_name)
        download_location = "./" 

        sendmsg = await bot.send_message(
            chat_id=message.chat.id,
            text=scrimp.DOWNLOAD_START,
            reply_to_message_id=message.message_id
        )
        
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=media,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                scrimp.DOWNLOAD_START,
                sendmsg,
                c_time
            )
        )
        if the_real_download_location is not None:
            try:
                await bot.edit_message_text(
                    text=scrimp.SAVED_RECVD_DOC_FILE,
                    chat_id=message.chat.id,
                    message_id=sendmsg.message_id
                )
            except:
                await sendmsg.delete()
                sendmsg = await message.reply_text(scrimp.SAVED_RECVD_DOC_FILE, quote=True)

            new_file_name = download_location + file_name + "." + extension
            os.rename(the_real_download_location, new_file_name)
            try:
                await bot.edit_message_text(
                    text=scrimp.UPLOAD_START,
                    chat_id=message.chat.id,
                    message_id=sendmsg.message_id
                    )
            except:
                await sendmsg.delete()
                sendmsg = await message.reply_text(scrimp.UPLOAD_START, quote=True)
            # logger.info(the_real_download_location)

            thumb_image_path = download_location + str(message.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                mes = await thumb(message.from_user.id)
                if mes != None:
                    m = await bot.get_messages(message.chat.id, mes.msg_id)
                    await m.download(file_name=thumb_image_path)
                    thumb_image_path = thumb_image_path
                else:
                    thumb_image_path = None                    
            else:
                width = 0
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                img.resize((320, height))
                img.save(thumb_image_path, "JPEG")

            c_time = time.time()
            await bot.send_document(
                chat_id=message.chat.id,
                document=new_file_name,
                thumb=thumb_image_path,
                caption=description,
                # reply_markup=reply_markup,
                reply_to_message_id=message.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    scrimp.UPLOAD_START,
                    sendmsg, 
                    c_time
                )
            )

            try:
                os.remove(new_file_name)
            except:
                pass                 
            try:
                os.remove(thumb_image_path)
            except:
                pass  
            try:
                await bot.edit_message_text(
                    text=scrimp.AFTER_SUCCESSFUL_UPLOAD_MSG,
                    chat_id=message.chat.id,
                    message_id=sendmsg.message_id,
                    disable_web_page_preview=True
                )
            except:
                await sendmsg.delete()
                await message.reply_text(scrimp.AFTER_SUCCESSFUL_UPLOAD_MSG, quote=True)
     
async def rename_as_video(bot, message):
    
    mssg = await bot.get_messages(
        message.chat.id,
        message.reply_to_message.message_id
    )    
    
    media = mssg.reply_to_message

    
    if media.empty:
        await message.reply_text('Why did you delete that 😕', True)
        return
        
    filetype = media.video or media.document
    try:
        actualname = filetype.file_name
        splitit = actualname.split(".")
        extension = (splitit[-1])
    except:
        extension = "mkv"

    await bot.delete_messages(
        chat_id=message.chat.id,
        message_ids=message.reply_to_message.message_id,
        revoke=True
    )
    
        file_name = message.text
        description = scrimp.CUSTOM_CAPTION_UL_FILE.format(newname=file_name)
        download_location = "./" 

        sendmsg = await bot.send_message(
            chat_id=message.chat.id,
            text=scrimp.DOWNLOAD_START,
            reply_to_message_id=message.message_id
        )
        
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=media,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                scrimp.DOWNLOAD_START,
                sendmsg,
                c_time
            )
        )
        if the_real_download_location is not None:
            try:
                await bot.edit_message_text(
                    text=scrimp.SAVED_RECVD_DOC_FILE,
                    chat_id=message.chat.id,
                    message_id=sendmsg.message_id
                )
            except:
                await sendmsg.delete()
                sendmsg = await message.reply_text(scrimp.SAVED_RECVD_DOC_FILE, quote=True)

            new_file_name = download_location + file_name + "." + extension
            os.rename(the_real_download_location, new_file_name)
            try:
                await bot.edit_message_text(
                    text=scrimp.UPLOAD_START,
                    chat_id=message.chat.id,
                    message_id=sendmsg.message_id
                    )
            except:
                await sendmsg.delete()
                sendmsg = await message.reply_text(scrimp.UPLOAD_START, quote=True)
            # logger.info(the_real_download_location)

            thumb_image_path = download_location + str(message.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                mes = await thumb(message.from_user.id)
                if mes != None:
                    m = await bot.get_messages(message.chat.id, mes.msg_id)
                    await m.download(file_name=thumb_image_path)
                    thumb_image_path = thumb_image_path
                else:
                    thumb_image_path = None                    
            else:
                width = 0
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                img.resize((320, height))
                img.save(thumb_image_path, "JPEG")

            c_time = time.time()
            await bot.send_video(
                chat_id=message.chat.id,
                document=new_file_name,
                thumb=thumb_image_path,
                caption=description,
                # reply_markup=reply_markup,
                reply_to_message_id=message.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    scrimp.UPLOAD_START,
                    sendmsg, 
                    c_time
                )
            )

            try:
                os.remove(new_file_name)
            except:
                pass                 
            try:
                os.remove(thumb_image_path)
            except:
                pass  
            try:
                await bot.edit_message_text(
                    text=scrimp.AFTER_SUCCESSFUL_UPLOAD_MSG,
                    chat_id=message.chat.id,
                    message_id=sendmsg.message_id,
                    disable_web_page_preview=True
                )
            except:
                await sendmsg.delete()
                await message.reply_text(scrimp.AFTER_SUCCESSFUL_UPLOAD_MSG, quote=True)
             
