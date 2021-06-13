# pmpermit for mafiaBot.....

import asyncio
import io
import os
import time

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

from userbot.plugins.sql_helper import pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, CUSTOM_PMPERMIT, MAFIA_ID
from userbot.Config import Config
from mafiabot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

PM_TRUE_FALSE = Config.PM_DATA

PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
MAFIAPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/a1720a18da7abfb6d4b66.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
h1m4n5hu0p = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "**Hɘɭɭo,, Its Sʌŋĸɩ Aʋtoɓot Pʀɩvʌtɘ Mʌssʌʛɘ Sɘcʋʀɩtƴ Assɩstʌŋt H3ʀ3."
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Sanki User"
USER_BOT_WARN_ZERO = "**Yoʋ wɘʀɘ spʌɱɱɩŋʛ ɱƴ swɘɘt ɱʌstɘʀ's ɩŋɓox, ʜɘŋcɘʆoʀtʜ ƴoʋ ʜʌvɘ ɓɘɘŋ ɓɭocĸɘɗ ɓƴ ɱƴ ɱʌstɘʀ's SʌŋĸɩAʋtoɓot.**\n__Now GTFO, ɩ'ɱ ɓʋsƴ__"
USER_BOT_NO_WARN = (
    "Dɘʌʀ, Lɩstɘŋ Mƴ Mʌstɘʀ Is Bʋsƴ Wʜɘŋ Tʜɘƴ Wɩɭɭ Bɘ Oŋɭɩŋɘ Hɘ Wɩɭɭ Msʛ Yoʋ Kɘɘp Cʌɭɱ.️**.\n"
    f"Its Mƴ Mʌstɘʀ {DEFAULTUSER}'s Iŋɓox.\n"
)

if Var.PRIVATE_GROUP_ID is not None:

    @borg.on(admin_cmd(pattern="allow|.a ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit(
                    "Appʀovɘɗ [{}](tg://user?id={}) to PM you.".format(
                        firstname, chat.id
                    )
                )
                await asyncio.sleep(3)
                await event.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit('`Rɘpɭƴ To Usɘʀ To Appʀovɘ Hɩɱ !`')
                return
            if not pmpermit_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pmpermit_sql.approve(reply_s.sender_id, "Appʀovɘɗ")
                await event.edit(
                        "Appʀovɘɗ [{}](tg://user?id={}) to pm.".format(firstname, reply_s.sender_id)
                    )
                await asyncio.sleep(3)
                await event.delete()
            elif pmpermit_sql.is_approved(reply_s.sender_id):
                await event.edit('`Usɘʀ Aɭʀɘʌɗƴ Appʀovɘɗ !`')
                await event.delete()

                

    # Approve outgoing
    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "__Aʋto-ʌppʀovɘɗ ɓcʋʑ oʋtʛoɩŋʛ 🚶__"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()

    @borg.on(admin_cmd(pattern="block ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1212368262 or chat.id == 816517310:
                await event.edit(
                    "Yoʋ tʀɩɘɗ to ɓɭocĸ ɱƴ ɱʌstɘʀ😡. GooɗBƴɘ ʆoʀ 100 sɘcoŋɗs !🥱😴😪💤"
                )
                time.sleep(100)
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "Gɘt ɭost ʀɘtʌʀɗ.\nBɭocĸɘɗ [{}](tg://user?id={})".format(
                            firstname, chat.id
                        )
                    )
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat.id))
        elif event.is_group:
            if chat.id == 1212368262 or chat.id == 816517310:
                await event.edit(
                    "Yoʋ tʀɩɘɗ to ɓɭocĸ ɱƴ ɱʌstɘʀ😡. GooɗBƴɘ ʆoʀ 100 sɘcoŋɗs !🥱😴😪💤"
                )
                time.sleep(100)
            else:
                reply_s = await event.get_reply_message()
                if not reply_s:
                    await event.edit('`Rɘpɭƴ To Usɘʀ To Bɭocĸ Hɩɱ !`')
                    return
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                if pmpermit_sql.is_approved(event.chat_id):
                    pmpermit_sql.disapprove(event.chat_id)
                await event.edit("Bɭocĸɘɗ [{}](tg://user?id={})".format(firstname, reply_s.sender_id))
                await event.client(functions.contacts.BlockRequest(reply_s.sender_id))
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(admin_cmd(pattern="disallow ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1212368262 or chat.id == 816517310:
                await event.edit("Soʀʀƴ, I Cʌŋ't Dɩsʌppʀovɘ Mƴ Mʌstɘʀ")
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "[{}](tg://user?id={}) ɗɩsʌppʀovɘɗ to PM.".format(
                            firstname, chat.id
                        )
                    )
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit('`Rɘpɭƴ To Usɘʀ To DɩsAppʀovɘ`')
                return
            if pmpermit_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pmpermit_sql.disapprove(reply_s.sender_id)
                await event.edit(
                    "Dɩsʌppʀovɘɗ [{}](tg://user?id={}) to PM.".format(firstname, reply_s.sender_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pmpermit_sql.is_approved(reply_s.sender_id):
                await event.edit('`Usɘʀ Not Appʀovɘɗ Yɘt`')
                await event.delete()    
                

    @borg.on(admin_cmd(pattern="listallowed"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Cʋʀʀɘŋtɭƴ Appʀovɘɗ PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "No Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="[MafiaBot]Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.sender_id == bot.uid:
            return

        if Var.PRIVATE_GROUP_ID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.sender_id

        message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return

        if PM_TRUE_FALSE == "DISABLE":
            return

        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == Config.MAX_FLOOD_IN_P_M_s:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except:
                return
        r = await borg.send_file(
            event.chat_id, MAFIAPIC, caption=USER_BOT_NO_WARN, force_document=False
        )
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r


# Do not touch the below codes!
@bot.on(events.NewMessage(incoming=True, from_users=(1212368262 or (816517310))))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(
                chat.id, "**Mƴ Boss ɩʑ ʜɘʀɘ.... It's ƴoʋʀ ɭʋcĸƴ ɗʌƴ ŋɩɓɓʌ😏**"
            )
            await borg.send_message(chat, "**Hɘʀɘ coɱɘs ɱƴ Mʌstɘʀ! Lʋcĸƴ ƴoʋ!!😏**")

CmdHelp("pmpermit").add_command(
  "allow|.a", "<pm use only>", "It allow the user to PM you."
).add_command(
  "disallow", "<pm use only>", "It disallows the user to PM. If user crosses the PM limit after disallow he/she will get blocked automatically"
).add_command(
  "block", "<pm use only>", "You know what it does.... Blocks the user"
).add_command(
  "listallowed", None, "Gives you the list of allowed PM's list"
).add_command(
  "set var PM_DATA", "DISABLE", "Turn off pm protection by your userbot. Your PM will not be protected."
).add()
