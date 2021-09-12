from telethon import events, Button, functions, types  
from PhoenixUb import phoenixub, phoenix, tag_log, mention

phoenix.parse_mode = "md"

@phoenixub.on(events.NewMessage(incoming=True, func=lambda e: (e.mentioned)))
async def taglog(slime):
  user=slime.sender
  kek = user.first_name
  chat = slime.chat
  msg = slime.message
  if msg.text:
    link = f"https://t.me/c/{chat.id}/{msg.id}"
    text = f"**{kek}** in **{chat.title}**\n\n`{msg.text}`"
    await phoenix.send_message(tag_log, text, buttons= [Button.url(text="Message", url = link)])
  elif msg.media:
    link = f"https://t.me/c/{chat.id}/{msg.id}"
    text = f"**{kek}** in **{chat.title}**\n\n`{msg.text}`"
    await phoenix.send_file(tag_log, file = msg.media, caption=text, buttons= [Button.url(text="Message", url = link)])
  else:
    pass
