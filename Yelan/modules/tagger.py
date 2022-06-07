import asyncio

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

from Yelan import client as telethn
from Yelan.events import register as nobara

from telegram.utils.helpers import escape_markdown, mention_html, mention_markdown


@nobara(pattern="^/tagall ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = str(event.pattern_match.group(1)).strip()
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n @{x.username}"
    await event.reply(mentions)
    await event.delete()


@nobara(pattern="^/users ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = "Users : "
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f" \n @{x.username}"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()


__mod_name__ = "Tagger"
__help__ = """
  × `/tagall` : Tag everyone in a chat
  × `/users` : Get user list
"""
