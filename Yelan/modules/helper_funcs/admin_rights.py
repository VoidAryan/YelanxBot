
from telegram import User, Chat
from Yelan import DEV_USERS, SUPPORT_USERS, DEMONS, WHITELIST_USERS

def user_can_promote(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_promote_members
    if (
        user.id in DEV_USERS
        or user.id in SUPPORT_USERS
    ):
        return True

def user_can_ban(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_restrict_members
    if (
        user.id in DEV_USERS
        or user.id in SUPPORT_USERS
    ):
        return True

def user_can_pin(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_pin_messages
    if (
        user.id in DEV_USERS
        or user.id in SUPPORT_USERS
    ):
        return True

def user_can_changeinfo(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_change_info


def user_can_delete(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_delete_messages
    if (
        user.id in DEV_USERS
        or user.id in SUPPORT_USERS
    ):
        return True
