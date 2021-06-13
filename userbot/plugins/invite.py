# Originally made by @rekcah for @javes05
# porting to hellbot by @kraken_the_badass...
# i asked rekcah before porting...not like other kangers....
# keep credit if u wanna kang...
# Now in mafiaBot
# else u are a gay...no doubt in that....

# --------------------------------------------------------------------------------------------------------------------------------

from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

from userbot import CMD_HELP
from mafiabot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`Tʜɩs ɩs ʌ pʀɩvʌtɘ cʜʌŋŋɘɭ/ʛʀoʋp oʀ I ʌɱ ɓʌŋŋɘɗ ʆʀoɱ tʜɘʀɘ`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Cʜʌŋŋɘɭ oʀ sʋpɘʀʛʀoʋp ɗoɘsŋ't ɘxɩst`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Iŋvʌɭɩɗ cʜʌŋŋɘɭ/ʛʀoʋp`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@bot.on(admin_cmd(pattern="inviteall ?(.*)"))
@bot.on(sudo_cmd(pattern="inviteall ?(.*)", allow_sudo=True))
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        mafia = await edit_or_reply(event, "`pʀocɘssɩŋʛ...`")
    else:
        mafia = await edit_or_reply(event, "`pʀocɘssɩŋʛ...`")
    kraken = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await mafia.edit("`Soʀʀƴ, Cʌŋt ĸɩɗŋʌpɘ ʋsɘʀs ʜɘʀɘ`")
    s = 0
    f = 0
    error = "None"

    await mafia.edit("**Tɘʀɱɩŋʌɭ Stʌtʋs**\n\n`ĸɩɗŋʌpɘɩŋʛ Usɘʀs.......`")
    async for user in event.client.iter_participants(kraken.full_chat.id):
        try:
            if error.startswith("Too"):
                return await mafia.edit(
                    f"**Tɘʀɱɩŋʌɭ Fɩŋɩsʜɘɗ Wɩtʜ Eʀʀoʀ**\n(`Mʌƴ Got Lɩɱɩt Eʀʀoʀ ʆʀoɱ tɘɭɘtʜoŋ Pɭɘʌsɘ tʀƴ ʌʛɩŋ Lʌtɘʀ`)\n**Eʀʀoʀ** : \n`{error}`\n\n• ĸɩɗŋʌpɘɗ `{s}` pɘopɭɘ \n• Fʌɩɭɘɗ to ĸɩɗŋʌpɘ `{f}` pɘopɭɘ"
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await mafia.edit(
                f"**Tɘʀɱɩŋʌɭ Rʋŋŋɩŋʛ...**\n\n• Iŋvɩtɘɗ `{s}` pɘopɭɘ \n• Fʌɩɭɘɗ to ĸɩɗŋʌpɘ `{f}` pɘopɭɘ\n\n**× LʌstEʀʀoʀ:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await mafia.edit(
        f"**Tɘʀɱɩŋʌɭ Fɩŋɩsʜɘɗ** \n\n• Sʋccɘssʆʋɭɭƴ ĸɩɗŋʌpɘɗ `{s}` pɘopɭɘ \n• Fʌɩɭɘɗ to ĸɩɗŋʌpɘ `{f}` pɘopɭɘ"
    )


@bot.on(admin_cmd(pattern="add ?(.*)"))
@bot.on(sudo_cmd(pattern="add ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await edit_or_reply(event, "`.add` users to a chat, not to a Private Message")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Iŋvɩtɘɗ Sʋccɘssʆʋɭɭƴ")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Aɗɗɘɗ ʋsɘʀ to tʜɘ cʜʌt....")


CmdHelp("invite").add_command(
  "add", "<username/id>", "Adds the given user to the group"
).add_command(
  "inviteall", "<group username>", "Scraps user from the targeted group to your group. Basically Kidnapps user from one chat to another"
).add()