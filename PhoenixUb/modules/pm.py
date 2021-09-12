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
  if not slime.media:
    await slime.forward_to(pm_log)
  else:
    await slime.forward_to(pm_log)
  if pm.is_approved(user.id):
    return 
  if user.id in now:
    count = now[user.id] 
    if count <= 5:
      await phoenixub.send_message(slime.chat_id,f"**Stop Spamming Saar** \n**Your Warns** : {count}/7")
      now[user.id] = count + 1
    elif count == 6:
      await phoenixub.send_message(slime.chat_id,"Spam More hehehe .., This is Your Last Chance😌")
      now[user.id] = count + 1
    elif count== 7:
      await phoenixub(functions.contacts.BlockRequest(id=user.id))
      await phoenixub.send_message(slime.chat_id, "Ewee, I Told You Not to Spam Now You are Blocked huh😒!.")
      time.sleep(2)
      await phoenixub.send_message(slime.chat_id, "Wait till My Master comes to approve you and found something useful in you ..")
      now[user.id] = 0
  else:
    now[user.id] = 0


@phoenixub.on(events.NewMessage(outgoing=True, pattern=r"^.(a|approve)($)"))    
async def approve(slime):
  if not slime.is_private:
    return 
  await slime.edit("✿Approving...")
  time.sleep(3)
  user = await slime.get_chat()
  h = pm.approve(user.id)
  if h == False:
    await slime.edit("⍟Already aprovved..")
    time.sleep(3)
    await slime.delete()
    return
  await slime.edit("Approval ✧ Successful!")
  time.sleep(3)
  await slime.delete()

@phoenixub.on(events.NewMessage(outgoing=True, pattern=r"^.(d|disapprove)($)"))    
async def approve(slime):
  if not slime.is_private:
    return 
  await slime.edit("✿Disapproving...")
  time.sleep(3)
  user = await slime.get_chat()
  h = pm.disapprove(user.id)
  if h == False:
    await slime.edit("⍟Already disaprovved..")
    time.sleep(3)
    await slime.delete()
    return
  await slime.edit("Disapproval ✧ Successful!")
  time.sleep(3)
  await slime.delete()
