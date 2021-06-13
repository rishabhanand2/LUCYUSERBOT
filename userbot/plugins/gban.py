from userbot import bot, CMD_HELP, ALIVE_NAME
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from mafiabot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
import html
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.events import ChatAction

HIMANSHU = str(ALIVE_NAME) if ALIVE_NAME else "Sanki User"
papa = borg.uid



async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_or_reply(event, "**Soɱ3tʜɩŋʛ W3ŋt Wʀ0ŋʛ**\n`Cʌŋ ƴoʋ pɭɘʌsɘ pʀovɩɗɘ ɱɘ ʌ ʋsɘʀ ɩɗ`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await edit_or_reply(event, "**Soɱ3tʜɩŋʛ W3ŋt Wʀ0ŋʛ**\n", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await edit_or_reply(event, str(err))
        return None
    return user_obj

@bot.on(admin_cmd(pattern="gban ?(.*)"))
@bot.on(sudo_cmd(pattern="gban ?(.*)", allow_sudo=True))
async def gban(userbot):
    if userbot.fwd_from:
        return
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        mafiabot = await edit_or_reply(ids, "Tʀƴɩŋʛ to ʛɓʌŋ tʜɩs ʀɘtʌʀɗ !")
    else:
        mafiabot = await edit_or_reply(ids, "`Oĸ! Gɓʌŋɩŋʛ tʜɩs pɩɘcɘ oʆ sʜɩt....`")
    hum = await userbot.client.get_me()
    await mafiabot.edit(f"`🔥Gɭoɓʌɭ Bʌŋ Iʑ Cʋɱɩŋ💦.... Wʌɩt ʌŋɗ wʌtcʜ ŋɩʛʛʌ🚶`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await mafiabot.edit(f"**Soɱ3tʜɩŋʛ W3ŋt Wʀ0ŋʛ 🤔**")
    if user:
        if user.id == 816517310 or user.id == 1212368262:
            return await mafiabot.edit(
                f"`Fɩʀst Gʀow Soɱɘ Bʌɭɭs To Gɓʌŋ Mƴ Cʀɘʌtɘʀ ʌŋɗ ɱƴ Cʀɘʌtɘʀs Fʀɘʌŋɗs🤫🚶`"
            )
        try:
            from userbot.plugins.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await mafiabot.edit(f"Gɓʌŋɩŋʛ Tʜɩs ʀɘtʌʀɗ🚶\n\n**Pɭɘʌsɘ Wʌɩt Fɘw Mɩŋʋtɘs**😏")
            except:
                b += 1
    else:
        await mafiabot.edit(f"`Eɩtʜɘʀ ʀɘpɭƴ to ʌ ʋsɘʀ oʀ ʛɩɓ ɱɘ ʋsɘʀ ɩɗ/ŋʌɱɘ`")
    try:        
        if gmute(user.id) is False:
            return await mafiabot.edit(f"**Eʀʀoʀ! Usɘʀ ʌɭʀɘʌɗƴ ʛɓʌŋŋɘɗ.**")
    except:
        pass
    return await mafiabot.edit(
        f"[{user.first_name}](tg://user?id={user.id}) Bɘtʌ ɱʌjɗʋʀ ĸo ĸʜoɗŋʌ ʌʋʀ [{Nɩtʀɩc}](tg://user?id={papa}) ĸo cʜoɗŋʌ ĸʌɓʜɩ sɩĸʜʌŋʌ ŋʜɩ.\n\n**Gɓʌŋ Sʋccɘssʆʋɭ 🔥\nAʆʆɘctɘɗ Cʜʌts😏 : {a} **"
    )

@bot.on(admin_cmd(pattern="ungban ?(.*)"))
@bot.on(sudo_cmd(pattern="ungban ?(.*)", allow_sudo=True))
async def gunban(userbot):
    if userbot.fwd_from:
        return
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        mafiabot = await edit_or_reply(ids, "`Tʀƴɩŋʛ to ʋŋʛɓʌŋ tʜɩs ĸɩɗ...`")
    else:
        mafiabot = await edit_or_reply(ids, "`Uŋʛɓʌŋ ɩŋ pʀoʛʀɘss...`")
    hum = await userbot.client.get_me()
    await mafiabot.edit(f"`Tʀƴɩŋʛ to ʋŋʛɓʌŋ tʜɩs ĸɩɗɗo...`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await mafiabot.edit("**Soɱ3tʜɩŋʛ W3ŋt Wʀ0ŋʛ**")
    if user:
        if user.id == 816517310 or user.id == 1212368262:
            return await mafiabot.edit("**Yoʋ ŋɘɘɗ to ʛʀow soɱɘ ɓʌɭɭs to ʛɓʌŋ / ʋŋʛɓʌŋ ɱƴ cʀɘʌtoʀ ʌŋɗ ʜɩs ʆʀɘʌŋɗs**")
        try:
            from userbot.plugins.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await mafiabot.edit(f"Oĸ! Now Uŋʛɓʌŋɩŋʛ tʜɩs ĸɩɗɗo.\n\n**Pɭɘʌsɘ Wʌɩt Fɘw Mɩŋʋtɘs**😏")
            except:
                b += 1
    else:
        await mafiabot.edit("**Rɘpɭƴ to ʌ ʋsɘʀ**")     
    try:
        if ungmute(user.id) is False:
            return await mafiabot.edit("**Eʀʀoʀ! I tʜɩŋĸ Usɘʀ ʌɭʀɘʌɗƴ ʋŋʛɓʌŋŋɘɗ.**")
    except:
        pass
    return await mafiabot.edit(
        f"**[{user.first_name}](tg://user?id={user.id}) Aʋʀ ɓʜʌɩ.... Aʌʛƴʌ swʌʌɗ.**\n\nUŋʛɓʌŋ Sʋccɘssʆʋɭ 🔥\nCʜʌts :- `{a}`"
    )




@borg.on(events.ChatAction)
async def handler(h1m4n5hu0p): 
   if h1m4n5hu0p.user_joined or h1m4n5hu0p.user_added:      
       try:       	
         from userbot.plugins.sql_helper.gmute_sql import is_gmuted
         guser = await h1m4n5hu0p.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await h1m4n5hu0p.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(h1m4n5hu0p.chat_id, guser.id, view_messages=False)                              
                    await h1m4n5hu0p.reply(
                     f"⚠️⚠️**Warning**⚠️⚠️\n\n`Gbanned User Joined the chat!!`\n"                      
                     f"**⚜️ Victim Id ⚜️**:\n[{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**🔥 Action 🔥**  :\n`Banned this piece of shit....` **AGAIN!**")                                                
                 except:       
                    h1m4n5hu0p.reply("`Shit!! No permission to ban users.\n@admins ban this retard.\nGlobally Banned User And A Potential Spammer`\n**Make your group a safe place by cleaning this shit**")                   
                    return
                  
                  
