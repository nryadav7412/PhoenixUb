from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio
import os 
import time

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
