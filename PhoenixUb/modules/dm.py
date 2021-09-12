from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio

@phoenixub.on(events.NewMessage(outgoing=True , pattern=".dm ?(.*)"))
async def dm(slime):
    args=slime.pattern_match.group(1)
    args=args.split(' ')
    if args[0]:
        reply=await slime.get_reply_message()
        await phoenixub.send_message(args[0] , reply)
        await slime.edit("`Message Sent!`")
        await asyncio.sleep(3)
        await slime.delete()
    

@phoenixub.on(events.NewMessage(outgoing=True , pattern=".save"))
async def save(slime):
    user=await phoenixub.get_me()
    reply=await e.get_reply_message()
    await phoenixub.send_message(user.username ,reply)
    await slime.edit(f"`Message Saved in Your saved msgs`")

@phoenixub.on(events.NewMessage(outgoing=True , pattern=".sco"))
async def sco(slime):
    args=slime.pattern_match.group(1)
    if not args:
          count=1
    else :
          count=int(args[0])
    reply=await slime.get_reply_message()
    await slime.delete()
    for i in range (count):
          await phoenixub.send_message(slime.chat_id,reply)
