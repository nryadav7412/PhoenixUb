from PhoenixUb import phoenixub, phoenix, pm_log, tag_log, mention
from telethon import events, Button, functions, types
from PhoenixUb.modules.sql import pm_sql as pm
import time

now = {}
phoenix.parse_mode='md'

@phoenixub.on(events.NewMessage(incoming=True))
async def pmperm(slime):
  global now
  if not slime.is_private:
    return
  user = await slime.get_chat()
  if user.bot:
    return
  name = mention(user.first_name, user.id)
  if not slime.media:
    await phoenix.send_message(pm_log, f"**{name}**: {slime.message.text}")
  else:
    await phoenix.send_file(pm_log, file=slime.media, caption=f"{name}: {slime.message.text}")
  if pm.is_approved(user.id):
    return 
  if user.id in now:
    count = now[user.id] 
    if count <= 5:
      await phoenixub.send_message(slime.chat_id,f"**Stop Spamming Saar** \n**Your Warns** : {count}")
      now[user.id] = count + 1
    elif count == 6:
      await phoenixub.send_message(slime.chat_id,"Spam More , This is Your Last Chance")
      now[user.id] = count + 1
    elif count== 7:
      await phoenixub(functions.contacts.BlockRequest(id=user.id))
      await phoenixub.send_message(slime.chat_id, "Agh, I Told You Not to Spam Now You are Blocked heheh.")
      time.sleep(2)
      await phoenixub.send_message(slime.chat_id, "Wait till My Master comes..")
      now[user.id] = 0
  else:
    now[user.id] = 0


@phoenixub.on(events.NewMessage(outgoing=True, pattern=r"^.(a|approve)($)"))    
async def approve(slime):
  if not slime.is_private:
    return 
  await slime.edit("✿Approving...")
  user = await slime.get_chat()
  h = pm.approve(user.id)
  if h == False:
    await slime.edit("⍟Already aprovved..")
    time.sleep(2)
    await slime.delete()
    return
  await slime.edit("✧Successful!")
  time.sleep(2)
  await slime.delete()

@phoenixub.on(events.NewMessage(outgoing=True, pattern=r"^.(d|disapprove)($)"))    
async def approve(slime):
  if not slime.is_private:
    return 
  await slime.edit("✿Disapproving...")
  user = await slime.get_chat()
  h = pm.disapprove(user.id)
  if h == False:
    await slime.edit("⍟Already disaprovved..")
    time.sleep(2)
    await slime.delete()
    return
  await slime.edit("✧Successful!")
  time.sleep(2)
  await slime.delete()
