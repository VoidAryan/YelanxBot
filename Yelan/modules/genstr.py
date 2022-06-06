import os
import json
import time
import asyncio

from asyncio.exceptions import TimeoutError
from YorForger import API_ID, API_HASH, pbot
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    SessionPasswordNeeded, FloodWait,
    PhoneNumberInvalid, ApiIdInvalid,
    PhoneCodeInvalid, PhoneCodeExpired
)

PHONE_NUMBER_TEXT = (
    "📞__ Send your Phone number to Continue"
    " include Country code.__\n**Eg:** `+13124562345`\n\n"
    "Press /cancel to Cancel."
)

cli = Client(":memory:", api_id=API_ID, api_hash=API_HASH)


@pbot.on_message(filters.private & filters.command("genstr"))
async def generate_str(c, m):
        get_phone_number = await c.ask(
            chat_id=m.chat.id,
            text=PHONE_NUMBER_TEXT
        )
        phone_number = get_phone_number.text
        if await is_cancel(m, phone_number):
            return
        await get_phone_number.delete()
        await get_phone_number.request.delete()

        confirm = await c.ask(
            chat_id=m.chat.id,
            text=f'🤔 Is `{phone_number}` correct? (y/n): \n\ntype: `y` (If Yes)\ntype: `n` (If No)'
        )
        if await is_cancel(m, confirm.text):
            return
        if "y" in confirm.text.lower():
            await confirm.delete()
            await confirm.request.delete()
        try:
            code = await client.send_code(phone_number)
            await asyncio.sleep(1)
        except FloodWait as e:
            await m.reply(f"__Sorry to say you that you have floodwait of {e.x} Seconds 😞__")
            return
        except PhoneNumberInvalid:
            await m.reply("☎ Your Phone Number is Invalid.`\n\nPress /genstr to create again.")
            return

        try:
           sent_type = {"app": "Telegram App 💌",
              "sms": "SMS 💬",
               "call": "Phone call 📱",
            "flash_call": "phone flash call 📲"
             }[code.type]
           otp = await c.ask(
               chat_id=m.chat.id,
               text=(f"I had sent an OTP to the number `{phone_number}` through {sent_type}\n\n"
                  "Please enter the OTP in the format `1 2 3 4 5` __(provied white space between numbers)__\n\n"
                  "If Bot not sending OTP then try /genstr to restart the module.\n"
                  "Press /cancel to Cancel."), timeout=300)
        except TimeoutError:
               await m.reply("**⏰ TimeOut Error:** You reached Time limit of 5 min.\nPress /genstr to create again.")
               return
        if await is_cancel(m, otp.text):
               return
        otp_code = otp.text
        await otp.delete()
        await otp.request.delete()
        try:
            await cli.sign_in(phone_number, code.phone_code_hash, phone_code=' '.join(str(otp_code)))
        except PhoneCodeInvalid:
            await m.reply("**📵 Invalid Code**\n\nPress /genstr to create again.")
            return 
        except PhoneCodeExpired:
            await m.reply("**⌚ Code is Expired**\n\nPress /genstr to create again.")
            return
        except SessionPasswordNeeded:
           try:
              two_step_code = await c.ask(
                   chat_id=m.chat.id, 
                   text="`🔐 This account have two-step verification code.\nPlease enter your second factor authentication code.`\nPress /cancel to Cancel.",
                   timeout=300
                 )
           except TimeoutError:
              await m.reply("**⏰ TimeOut Error:** You reached Time limit of 5 min.\nPress /start to create again.")
              return
           if await is_cancel(m, two_step_code.text):
              return
           new_code = two_step_code.text
           await two_step_code.delete()
           await two_step_code.request.delete()
           try:
               await cli.check_password(new_code)
           except Exception as e:
               await m.reply(f"**⚠️ ERROR:** `{str(e)}`")
               return
           except Exception as e:
               await c.send_message(m.chat.id ,f"**⚠️ ERROR:** `{str(e)}`")
               return
           try:
               session_string = await client.export_session_string()
               await client.send_message(m.chy.id, f"**Your String Session 👇**\n\n`{session_string}`\n\nThanks For using {(await c.get_me()).mention(style='md')}")
           except Exception as e:
               await c.send_message(m.chat.id ,f"**⚠️ ERROR:** `{str(e)}`")
               return
           try:
               await client.stop()
           except:
               pass

async def is_cancel(msg: Message, text: str):
    if text.startswith("/cancel"):
        await msg.reply("⛔ Process Cancelled.")
        return True
    return False


__mod_name__ = "GenStr"
__help__ = """
*Here is help for GenStr*

This Module Can Be Used To Generate Session String For A Userbot.
Send /genstr Command To The Bot In Private And Follow Instructions.

Note : You Are Free To Revoke Session String This Bot Generate So It's Safe.
"""
