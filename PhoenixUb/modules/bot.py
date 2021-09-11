from PhoenixUb import phoenixub, phoenix, mention, alive_pic, help_strings
from telethon import events, Button
from datetime import datetime as dt

@phoenixub.on(events.NewMessage(outgoing=True, pattern=r'^.(alive)'))
async def alive(slime):
  me = await phoenixub.get_me()
  date = dt.now()
  date = date.strftime("%B %d, %Y")
  kek = mention(me.first_name, me.id)
  await slime.delete()
  await phoenixub.send_file(slime.chat_id , alive_pic , caption=f"**「 Phoenix Userbot ..」**\n**My Master** : {kek}\n**Date** : {date}")
  await slime.delete()
  
@phoenixub.on(events.NewMessage(outgoing=True, pattern=r'^.ping$'))
async def ping(slime):
  start = dt.now()
  await slime.edit("`۞Pinging....`")
  end = dt.now()
  pon = (start - end).microseconds / 1000
  await slime.edit(f"`Pong !!` \n`PongTime` : {pon} ms")

@phoenix.on(events.NewMessage(incoming=True,pattern=r'^\/start'))
async def start(slime):
  bot = await phoenix.get_me()
  user = await phoenixub.get_me()
  text = f'''Hello Telegram User , I am [{bot.first_name}](https://t.me/{bot}.username) ,a userbot and helper for {{user.first_name}](https://t.me/{user}.username)'''
  await slime.reply(text)
