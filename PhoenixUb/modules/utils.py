from PhoenixUb import phoenixub, phoenix
from telethon import events, Button
from telethon.utils import pack_bot_file_id
import time 

helper = '''
`.purge`: reply to message to delete every message till the latest message 
`.id`: reply to anything to get the respective ids 
'''

@phoenixub.on(events.NewMessage(outgoing=True,pattern=r".purge(.*)"))
async def purge(slime):
  msg = slime.message.text.split(" ", 3)
  reply = await slime.get_reply_message()
  if not reply:
    await slime.edit("Reply...")
    time.sleep(1)
    await slime.delete()
  from_msg = reply.id - 1
  try:
    to_msg = msg[2]
  except IndexError:
    to_msg = False 
  count = 0
  async for msg in phoenixub.iter_messages(slime.chat_id, reverse=True, offset_id=from_msg):
    if not to_msg == False:
      if count == int(to_msg):
        break 
    try:
      await msg.delete()
      count += 1
    except Exception:
      pass
  if not count == 0:
    xx=await slime.respond(f"Purged {count} messages..")
    time.sleep(3)
    await xx.delete()
    
@phoenixub.on(events.NewMessage(outgoing=True, pattern=r'^.id'))    
async def idscrape(slime):
    if slime.reply_to_msg_id:
        await slime.get_input_chat()
        r_msg = await slime.get_reply_message()
        await slime.edit("**User ID:**  `{}`".format(str(r_msg.sender_id)))
    else:
        await slime.edit("**Current Chat ID:**  `{}`".format(str(slime.chat_id)))
