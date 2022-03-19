from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio
import os 
import time
import pytz
from datetime import datetime
from pytz import timezone
from telegraph import upload_file as uf

@phoenixub.on(events.NewMessage(outgoing=True , pattern=".dc ?(.*)"))
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit("Bsdk Give Name.")
        await asyncio.sleep(3)
        await event.delete()
    if event.reply:
        a = await event.get_reply_message()
        if not a.message:
            return await event.edit("Reply to a message")
        else:
            b = open(input_str, "w")
            b.write(str(a.message))
            b.close()
            await event.edit(f"Packing into {input_str}")
            await phoenixub.send_file(
                event.chat_id, input_str,caption=str(f"""`{input_str}`""")
            )
            await event.delete()
            os.remove(input_str)
            
@phoenixub.on(events.NewMessage(outgoing=True , pattern=".open"))
async def _(event):
    if event.reply:
        a = await event.get_reply_message()
        if not a.message:
            return await event.edit("Reply to a message")
        else:
            dl=await a.download_media()
            nm=a.file.name
            b = open(nm, "r")
            data=b.read()
            b.close()
            await event.edit(f"`{data}`")
            os.remove(nm)
            
@phoenixub.on(events.NewMessage(outgoing=True , pattern=".telegraph"))
async def telegraph(event):
    reply=await event.get_reply_message()
    await event.edit("`Pasting to telegraph...`")
    dl=await reply.download_media()
    tt=uf(dl)
    limk="https://telegra.ph" + tt[0]
    await event.edit(f"`Uploaded To Telegraph` : `{limk}`")

@phoenixub.on(events.NewMessage(outgoing=True , pattern=".when"))
async def _(event):
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    format="%d-%m-%Y %H:%M:%S %Z%z"
    op=result.astimezone(timezone('Asia/Kolkata'))
    go= datetime.now(timezone('Asia/Kolkata'))
    diff=go-op
    diff=str(diff)
    args=diff.split(':')
    hrs=args[0]
    min=args[1]
    second=args[2]
    sec=second.split('.')
    second=sec[0]
    result=op.strftime(format)
    await event.edit(str(f"""`This message was posted on : {result} which is {hrs} hours {min} minutes {second} seconds ago   `"""))
    
@phoenixub.on(events.NewMessage(chats=-1001728926527))
async def my_event_handler(event):
    if event.photo:
        if event.text:
            await phoenixub.send_file(-1001669984404,event.media,caption=event.text)
            await phoenixub.send_file(-1001648592978,event.media,caption=event.text)
            await phoenixub.send_file(-1001604562578,event.media,caption=event.text)
            await phoenixub.send_file(-1001788857163,event.media,caption=event.text)
            await phoenixub.send_file(-1001633246713,event.media,caption=event.text)
        else:
            await phoenixub.send_file(-1001669984404,event.media)
            await phoenixub.send_file(-1001648592978,event.media)
            await phoenixub.send_file(-1001604562578,event.media)
            await phoenixub.send_file(-1001788857163,event.media)
            await phoenixub.send_file(-1001633246713,event.media)
    elif event.text:
        if not event.document:
            await phoenixub.send_message(-1001669984404,event.text)
            await phoenixub.send_message(-1001648592978,event.text)
            await phoenixub.send_message(-1001604562578,event.text)
            await phoenixub.send_message(-1001788857163,event.text)
            await phoenixub.send_message(-1001633246713,event.text)
    if event.video:
        if event.text:
            await phoenixub.send_file(-1001669984404,event.media,caption=event.text)
            await phoenixub.send_file(-1001648592978,event.media,caption=event.text)
            await phoenixub.send_file(-1001604562578,event.media,caption=event.text)
            await phoenixub.send_file(-1001788857163,event.media,caption=event.text)
            await phoenixub.send_file(-1001633246713,event.media,caption=event.text)
        else:
            await phoenixub.send_file(-1001669984404,event.media)
            await phoenixub.send_file(-1001648592978,event.media)
            await phoenixub.send_file(-1001604562578,event.media)
            await phoenixub.send_file(-1001788857163,event.media)
            await phoenixub.send_file(-1001633246713,event.media)
            
@phoenixub.on(events.NewMessage(chats=-1001737438474))
async def mkv(event):
    a=event.raw_text
    lists=a.split(' ')
    title='🎬'+'Title: '+lists[0]+' '+lists[1]
    x=lists[2:-3]
    episode=''
    for i in x:
      episode+=i+' '
    episode=episode
    episode=episode[1:-2]
    language=lists[-3]
    language=language[1:-1]
    language=language.replace('-',' + ')
    await event.edit(str(f'''**{title}**
**📟Episode: {episode}**
**🔊Language: {language}**
**📀Quality: 720p**
 
 
**❤️‍🔥@Pokemon_Episodess❤️‍🔥**'''))
    
@phoenixub.on(events.NewMessage(outgoing=True , pattern=".demote ?(.*)"))
async def demote(event):
    xx = await event.edit("`Demoting...`")
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.sender_id
    else:
        args=event.pattern_match.group(1)
        sendr=args.strip()
    try:
        await phoenixub.edit_admin(
            event.chat_id,
            int(sendr),
            invite_users=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None,
            manage_call=None,
            title=rank,
        )
        await event.edit(f"Succesfully Demoted `{sendr}` here...")
    except Exception as ex:
        return await xx.edit(f"`{ex}`")

@phoenixub.on(events.NewMessage(outgoing=True , pattern=".ban ?(.*)"))
async def ban(event):
    xx = await event.edit("`Banning...`")
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.sender_id
    else:
        args=event.pattern_match.group(1)
        sendr=args.strip()
    try:
        await phoenixub.edit_permissions(event.chat_id, int(sendr), view_messages=False)
        await event.edit(f"Succesfully Banned This Person Here...")
    except Exception as e:
        await event.edit(f"{e}")

@phoenixub.on(events.NewMessage(outgoing=True , pattern=".unban ?(.*)"))
async def unban(event):
    xx = await event.edit("`UnBanning...`")
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.sender_id
    else:
        args=event.pattern_match.group(1)
        sendr=args.strip()
    try:
        await phoenixub.edit_permissions(event.chat_id, int(sendr), view_messages=True)
        await event.edit(f"Succesfully UnBanned This Person Here...")
    except Exception as e:
        await event.edit(f"{e}")
        
@phoenixub.on(events.NewMessage(outgoing=True , pattern=".kick ?(.*)"))
async def unban(event):
    xx = await event.edit("`Kicking...`")
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.sender_id
    else:
        args=event.pattern_match.group(1)
        sendr=args.strip()
    try:
        await phoenixub.kick_participant(event.chat_id, int(sendr))
        await event.edit(f"Succesfully Kicked This Person Here...")
    except Exception as e:
        await event.edit(f"{e}")
        
@phoenixub.on(events.NewMessage(outgoing=True , pattern=".pin"))
async def unban(event):
    xx = await event.edit("`Pinning...`")
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.id
    else:
        await event.edit("`Reply...`")
    try:
        await phoenixub.pin_message(event.chat_id, sendr, notify=False)
        await event.edit(f"Pinned...")
    except Exception as e:
        pass
    
@phoenixub.on(events.NewMessage(outgoing=True , pattern=".unpin"))
async def unban(event):
    xx = await event.edit("`UnPinning...`")
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.id
    else:
        await event.edit("`Reply...`")
    try:
        await phoenixub.unpin_message(event.chat_id, sendr)
        await event.edit(f"UnPinned...")
    except Exception as e:
        pass
    
@phoenixub.on(events.NewMessage(outgoing=True , pattern=".mute ?(.*)"))
async def mute(event):
    xx=await event.edit("`Muting...`")
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.sender_id
    else:
        args=event.pattern_match.group(1)
        sendr=args.strip()
    try:
        await phoenixub.edit_permissions(
            event.chat_id,
            int(sendr),
            until_date=None,
            send_messages=False,
        )
        await event.edit(f"`Successfully Muted {sendr}  Here`")
    except Exception as m:
        await event.edit(f"{m}")

@phoenixub.on(events.NewMessage(outgoing=True , pattern=".unmute ?(.*)"))
async def unmute(event):
    xx=await event.edit("`UnMuting...`")
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.sender_id
    else:
        args=event.pattern_match.group(1)
        sendr=args.strip()
    try:
        await phoenixub.edit_permissions(
            event.chat_id,
            int(sendr),
            until_date=None,
            send_messages=True,
        )
        await event.edit(f"`Successfully UnMuted {sendr}  Here`")
    except Exception as m:
        await event.edit(f"{m}")        
    
@phoenixub.on(events.NewMessage(outgoing=True , pattern=".promote ?(.*)"))
async def promote(event):
    xx = await event.edit("`Promoting...`")
    rank = "Admin"
    if event.reply:
        a=await event.get_reply_message()
        sendr=a.sender_id
    else:
        args=event.pattern_match.group(1)
        sendr=args.strip()
    try:
        await phoenixub.edit_admin(
            event.chat_id,
            int(sendr),
            invite_users=True,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
            manage_call=True,
            title=rank,
        )
        await event.edit(f"Now `{sendr}` is Admin Here...")
    except Exception as ex:
        return await xx.edit(f"`{ex}`")
