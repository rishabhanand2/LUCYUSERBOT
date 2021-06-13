from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio
from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
from telethon import events


@bot.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"gmute ?(\d+)?", allow_sudo=True))
async def blowjob(event):
    private = False
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    user_id = reply.sender_id
    if user_id == (await borg.get_me()).id:	
        await edit_or_reply(event, "I ʛʋɘss ƴoʋ ŋɘɘɗ soɱɘ ʀɘst. Yoʋ ʌʀɘ tʀƴɩŋʛ to ʛɱʋtɘ ƴoʋʀsɘɭʆ😌")	
        	
        return
    elif event.is_private:
        await edit_or_reply(event, "`Sʜʋt Uʀ Moʋtʜ Cɭosɘ Aŋɗ Sʋcĸ Mƴ Dɩcĸ :) 🤐. Filled mouth with cum`💦")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(event, "I ŋɘɘɗ ʌ ʋsɘʀ to ʛɱʋtɘ. Pɭɘʌsɘ ʀɘpɭƴ oʀ ʛɘt ʜɩs ʋɩɗ")
    chat_id = event.chat_id
    chat = await event.get_chat()
    if is_muted(userid, "gmute"):
        return await edit_or_reply(event, "Tʜɩs ʀɘtʌʀɗ cʌŋt spɘʌĸ. Wʌs ʌɭʀɘʌɗƴ ʛɱʋttɘɗ ɘʌʀɭɩɘʀ")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Eʀʀoʀ occʋʀɘɗ !\nEʀʀoʀ ɩs " + str(e))
    else:
        await edit_or_reply(event, "Sʋccɘssʆʋɭɭƴ Fʋcĸɘɗ tʜɩs ʋsɘʀ's ɱoʋtʜ.")


@bot.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"ungmute ?(\d+)?", allow_sudo=True))
async def cumshot(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await edit_or_reply(event, "Toɗʌƴ's sɘx ɗoŋɘ. Now soŋ cʌŋ spɘʌĸ✌️🚶")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(event, "Pɭɘʌsɘ ʀɘpɭƴ to ʌ ʋsɘʀ oʀ ʌɗɗ tʜɘɱ ɩŋto tʜɘ coɱɱʌŋɗ to ʋŋʛɱʋtɘ tʜɘɱ.")
    chat_id = event.chat_id
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(event, "Tʜɩs ʋsɘʀ cʌŋ ʌɭʀɘʌɗƴ spɘʌĸ ʆʀɘɘɭƴ✌️😃")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Eʀʀoʀ occʋʀɘɗ !\nEʀʀoʀ ɩs " + str(e))
    else:
        await edit_or_reply(event, "Oĸ ! Toɗʌƴ's sɘx ɩs ɗoŋɘ ŋow. Soŋ cʌŋ spɘʌĸ🔥🔥")
        
@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
