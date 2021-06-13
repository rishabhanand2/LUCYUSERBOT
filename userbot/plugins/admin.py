# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
"""
Userbot module to help you manage a group
"""

from asyncio import sleep

from telethon import functions
from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
    MessageMediaPhoto,
)

from userbot import *
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
from mafiabot.utils import *
from userbot.cmdhelp import CmdHelp

# =================== CONSTANT ===================

PP_TOO_SMOL = "`Tʜɘ ɩɱʌʛɘ ɩs too sɱʌɭɭ`"
PP_ERROR = "`Fʌɩɭʋʀɘ wʜɩɭɘ pʀocɘssɩŋʛ tʜɘ ɩɱʌʛɘ`"
NO_ADMIN = "`I ʌɱ ŋot ʌŋ ʌɗɱɩŋ! Cʜʋtɩƴʌ sʌɭʌ`"
NO_PERM = "`I ɗoŋ't ʜʌvɘ sʋʆʆɩcɩɘŋt pɘʀɱɩssɩoŋs! Sɘɗ -_-`"
CHAT_PP_CHANGED = "`Cʜʌt Pɩctʋʀɘ Cʜʌŋʛɘɗ Sʋccɘssʆʋɭɭƴ`"
INVALID_MEDIA = "`Iŋvʌɭɩɗ ɱɘɗɩʌ Extɘŋsɩoŋ`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# ================================================


@bot.on(admin_cmd("setgpic$"))
@bot.on(sudo_cmd(pattern="setgpic$", allow_sudo=True))
@errors_handler
async def set_group_photo(gpic):
    if gpic.fwd_from:
        return
    if not gpic.is_group:
        await edit_or_reply(gpic, "`I ɗoŋ't tʜɩŋĸ tʜɩs ɩs ʌ ʛʀoʋp.`")
        return
    replymsg = await gpic.get_reply_message()
    chat = await gpic.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    photo = None
    if not admin and not creator:
        await edit_or_reply(gpic, NO_ADMIN)
        return
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await edit_or_reply(gpic, INVALID_MEDIA)
    h1m4n5hu0p = None
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await gpic.client.upload_file(photo))
            )
            await edit_or_reply(gpic, CHAT_PP_CHANGED)
            h1m4n5hu0p = True
        except PhotoCropSizeSmallError:
            await edit_or_reply(gpic, PP_TOO_SMOL)
        except ImageProcessFailedError:
            await edit_or_reply(gpic, PP_ERROR)
        except Exception as e:
            await edit_or_reply(gpic, f"**Eʀʀoʀ : **`{str(e)}`")
        if BOTLOG and h1m4n5hu0p:
            await gpic.client.send_message(
                BOTLOG_CHATID,
                "#GROUPPIC\n"
                f"Gʀoʋp pʀoʆɩɭɘ pɩc cʜʌŋʛɘɗ "
                f"CHAT: {gpic.chat.title}(`{gpic.chat_id}`)",
            )


@bot.on(admin_cmd("promote(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="promote(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def promote(promt):
    if promt.fwd_from:
        return
    chat = await promt.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(promt, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    mafiaevent = await edit_or_reply(promt, "Pʀoɱotɩŋʛ Pɭʑ Wʌɩt...")
    user, rank = await get_user_from_event(promt)
    if not rank:
        rank = "Sʌŋĸɩ Wʌʀʀɩoʀs <3"
    if not user:
        return
    try:
        await promt.client(EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await mafiaevent.edit("Pʀoɱotɘɗ Sʋccɘssʆʋɭɭƴ ! Cʜʌɭ Kʜʋsʜ Hojʌ Aɓ Dʜʌŋŋo <3")
    except BadRequestError:
        await mafiaevent.edit(NO_PERM)
        return
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID,
            "#PROMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {promt.chat.title}(`{promt.chat_id}`)",
        )


@bot.on(admin_cmd("demote(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="demote(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def demote(dmod):
    if dmod.fwd_from:
        return
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(dmod, NO_ADMIN)
        return
    mafiaevent = await edit_or_reply(dmod, "Dɘɱotɩŋʛ Pɭʑ Wʌɩt...")
    rank = "Sʌŋĸɩ Wʌʀʀɩoʀs <3"
    user = await get_user_from_event(dmod)
    user = user[0]
    if not user:
        return
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    try:
        await dmod.client(EditAdminRequest(dmod.chat_id, user.id, newrights, rank))
    except BadRequestError:
        await mafiaevent.edit(NO_PERM)
        return
    await mafiaevent.edit("Dɘɱotɘɗ Sʋccɘssʆʋɭɭƴ ! Nɩĸʌɭ Bsɗĸ.")
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID,
            "#DEMOTE\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)",
        )


@bot.on(admin_cmd("ban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="ban(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def ban(bon):
    if bon.fwd_from:
        return
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(bon, NO_ADMIN)
        return
    user, reason = await get_user_from_event(bon)
    if not user:
        return
    mafiaevent = await edit_or_reply(bon, "Bʌŋŋɩŋʛ tʜɩs Sʋʌʀ Wʌɩt...")
    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await mafiaevent.edit(NO_PERM)
        return
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await mafiaevent.edit("I ʌɩŋ't ʛot ɱsʛ ɗɘɭɘtɩŋʛ ʀɩʛʜt. Bʋt stɩɭɭ Bʌŋŋɘɗ !")
        return
    if reason:
        await mafiaevent.edit(f"{str(user.id)} ɩs ɓʌŋŋɘɗ !!\nRɘʌsoŋ : {reason}")
    else:
        await mafiaevent.edit(f"{str(user.id)} ɩs ɓʌŋŋɘɗ !!")
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID,
            "#BAN\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {bon.chat.title}({bon.chat_id})",
        )


@bot.on(admin_cmd("unban(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="unban(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def nothanos(unbon):
    if unbon.fwd_from:
        return
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(unbon, NO_ADMIN)
        return
    mafiaevent = await edit_or_reply(unbon, "Uŋɓʌŋŋɩŋʛ Pɭʑ Wʌɩt...")
    user = await get_user_from_event(unbon)
    user = user[0]
    if not user:
        return
    try:
        await unbon.client(EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await mafiaevent.edit("Uŋɓʌŋŋɘɗ Sʋccɘssʆʋɭɭƴ ! Cʜʌɭ Kʜʋsʜ Hojʌ Aɓ Dʜʌŋŋo <3")
        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID,
                "#UNBAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)",
            )
    except UserIdInvalidError:
        await mafiaevent.edit("Soʀʀƴ I Cʌŋ't Uŋɓʌŋ !")


@command(incoming=True)
async def watcher(event):
    if event.fwd_from:
        return
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))

@bot.on(admin_cmd("pin($| (.*))"))
@bot.on(sudo_cmd(pattern="pin($| (.*))", allow_sudo=True))
@errors_handler
async def pin(msg):
    if msg.fwd_from:
        return
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(msg, NO_ADMIN)
        return
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        await edit_or_reply(msg, "Rɘpɭƴ to ʌ ɱɘssʌʛɘ to pɩŋ ɩt.")
        return
    options = msg.pattern_match.group(1)
    is_silent = True
    if options.lower() == "loud":
        is_silent = False
    try:
        await msg.client(UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except BadRequestError:
        await edit_or_reply(msg, NO_PERM)
        return
    hmm = await edit_or_reply(msg, "Pɩŋŋɘɗ Sʋccɘssʆʋɭɭƴ !")
    user = await get_user_from_id(msg.sender_id, msg)
    if BOTLOG:
        await msg.client.send_message(
            BOTLOG_CHATID,
            "#PIN\n"
            f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {msg.chat.title}(`{msg.chat_id}`)\n"
            f"LOUD: {not is_silent}",
        )
    await sleep(3)
    try:
        await hmm.delete()
    except:
        pass


@bot.on(admin_cmd("kick(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="kick(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def kick(usr):
    if usr.fwd_from:
        return
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(usr, NO_ADMIN)
        return
    user, reason = await get_user_from_event(usr)
    if not user:
        await edit_or_reply(usr, "Coʋɭɗŋ't ʆɘtcʜ ʋsɘʀ.")
        return
    mafiaevent = await edit_or_reply(usr, "Kicking...")
    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        await mafiaevent.edit(NO_PERM + f"\n{str(e)}")
        return
    if reason:
        await mafiaevent.edit(
            f"Kɩcĸɘɗ [{user.first_name}](tg://user?id={user.id})!\nRɘʌsoŋ: {reason}"
        )
    else:
        await mafiaevent.edit(f"Kɩcĸɘɗ [{user.first_name}](tg://user?id={user.id})!")
    if BOTLOG:
        await usr.client.send_message(
            BOTLOG_CHATID,
            "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {usr.chat.title}({usr.chat_id})\n",
        )


@bot.on(admin_cmd("undlt$"))
@bot.on(sudo_cmd(pattern="undlt$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.fwd_from:
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await event.client.get_admin_log(
            event.chat_id, limit=5, edit=False, delete=True
        )
        deleted_msg = "Dɘɭɘtɘɗ ɱɘssʌʛɘ ɩŋ tʜɩs ʛʀoʋp :"
        for i in a:
            deleted_msg += "\n👉{}".format(i.old.message)
        await edit_or_reply(event, deleted_msg)
    else:
        await edit_or_reply(
            event, "Yoʋ ŋɘɘɗ ʌɗɱɩŋɩstʀʌtɩvɘ pɘʀɱɩssɩoŋs ɩŋ oʀɗɘʀ to ɗo tʜɩs coɱɱʌŋɗ"
        )
        await sleep(3)
        try:
            await event.delete()
        except:
            pass


async def get_user_from_event(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif args:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("Pʌss tʜɘ ʋsɘʀ's ʋsɘʀŋʌɱɘ, ɩɗ oʀ ʀɘpɭƴ !")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError):
            await event.edit("Coʋɭɗ ŋot ʆɘtcʜ ɩŋʆo oʆ tʜʌt ʋsɘʀ.")
            return None
    return user_obj, extra


async def get_user_from_id(user, event):
    if event.fwd_from:
        return
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

CmdHelp("admin").add_command(
       'setgpic', '<reply to image>', 'Changes the groups display picture'
).add_command(
        'promote', '<username/reply> <custom rank (optional)>',
        'Provides admins right to a person in the chat.'
).add_command(
        'demote', '<username/reply>', 'Revokes the person admin permissions    in the chat.'
).add_command(
        'ban', '<username/reply> <reason (optional)>', 'Bans the person off your chat.'
).add_command(
        'unban', '<username/reply>', 'Removes the ban from the person in the chat.'
).add_command(
        'mute', '<username/reply> <reason (optional)>', 'Mutes the person in the chat, works on admins too.'
).add_command(
        'unmute', '<username/reply>', 'Removes the person from the muted list.'
).add_command(
        'pin', '<reply> or .pin loud', 'Pins the replied message in Group'
).add_command(
        'kick', '<username/reply>', 'kick the person off your chat'
).add_command(
        'iundlt', None, 'display last 5 deleted messages in group.'
).add()
