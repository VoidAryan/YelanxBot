import asyncio
import traceback

from pyrogram import filters
from pyrogram.types import ChatPermissions
from Yelan import OWNER_ID
import os 


from Yelan import DEV_USERS, SUPPORT_USERS
from Yelan import BOT_ID, pbot as app




async def member_permissions(chat_id: int, user_id: int):
    perms = []
    member = await app.get_chat_member(chat_id, user_id)
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_voice_chats:
        perms.append("can_manage_voice_chats")
    return perms


async def current_chat_permissions(chat_id):
    perms = []
    perm = (await app.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_stickers:
        perms.append("can_send_stickers")
    if perm.can_send_animations:
        perms.append("can_send_animations")
    if perm.can_send_games:
        perms.append("can_send_games")
    if perm.can_use_inline_bots:
        perms.append("can_use_inline_bots")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")

    return perms


@app.on_message(filters.command("fullpromote"))
async def fmupromote(_, message):
    try:
        from_user_id = message.from_user.id
        chat_id = message.chat.id
        permissions = await member_permissions(chat_id, from_user_id)
        if (
            "can_promote_members" not in permissions
            and from_user_id not in DEV_USERS
        ):
            await message.reply_text("You don't have enough permissions")
            return
        bot = await app.get_chat_member(chat_id, BOT_ID)
        if len(message.command) == 2:
            username = message.text.split(None, 1)[1]
            user_id = (await app.get_users(username)).id
        elif len(message.command) == 1 and message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            await message.reply_text(
                "Reply To A User's Message Or Give A Username To Promote."
            )
            return
        await message.chat.promote_member(
            user_id=user_id,
            can_change_info=bot.can_change_info,
            can_invite_users=bot.can_invite_users,
            can_delete_messages=bot.can_delete_messages,
            can_restrict_members=True,
            can_pin_messages=bot.can_pin_messages,
            can_promote_members=bot.can_promote_members,
            can_manage_chat=bot.can_manage_chat,
            can_manage_voice_chats=bot.can_manage_voice_chats,
        )
        await message.reply_text("Sucessfully Full Promoted this user!")

    except Exception as e:
        await message.reply_text(str(e))
        e = traceback.format_exc()
        print(e)

