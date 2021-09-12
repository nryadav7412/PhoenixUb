from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio

@phoenixub.on(pattern="dm ?(.*)")
async def dm(e):
    if len(e.text) > 3:
        if not e.text[3] == " ":  # weird fix
            return
    d = e.pattern_match.group(1)
    c = d.split(" ")
    try:
        chat_id = await get_user_id(c[0])
    except Exception as ex:
        return await eod(e, "`" + str(ex) + "`")
    msg = ""
    masg = await e.get_reply_message()
    if e.reply_to_msg_id:
        await phoenixub.send_message(chat_id, masg)
        await e.edit("`Message Sent!`")
    for i in c[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await phoenixub.send_message(chat_id, msg)
        await e.edit("`Message Sent!`")
    except BaseException:
        await eod(e, f"Use Properly Saar : `.dm <reply>/.dm <username> <msg>`")
