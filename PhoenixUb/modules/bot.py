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
  await slime.edit(f'''🏓 PONG!!
⚡️ {pon} ms''')

@phoenix.on(events.NewMessage(incoming=True,pattern=r'^\/start'))
async def start(slime):
  bot = await phoenix.get_me()
  user = await phoenixub.get_me()
  text = f'''Hello Telegram User , I am **{bot.first_name}** ,a userbot and helper for **{user.first_name}**'''
  await slime.reply(text)

@phoenixub.on(events.NewMessage(outgoing=True, pattern=".help ?(.*)"))
async def help(slime):
  args=slime.pattern_match.group(1)
  if not args:
    await slime.edit(f'''**Your Userbot Has Following plugins Installed** :-
1. `bot`
2. `pm`
3. `songs`
4. `utils`
5.  `tag`
6.  `dm`

**You check commands for each plugin by** `.help <plugin name>`''')
  elif args=='bot':
    await slime.edit(f'''**This plugin has:**
`.alive` : Check If our Bot Alive
`.ping` : Check Pong Time
`.help` : Check Help menu''')
  elif args=='pm':
    await slime.edit(f'''**This plugin has :**
`.a` / `.approve` : To approve
`.d` / `.disapprove` : To Disapprove''')
  elif args=='songs':
    await slime.edit(f'''**This plugin has :**
`.song <song>`: Get the Song From Youtube''')
  elif args=='utils':
    await slime.edit(f'''**This plugin has :**
`.purge`: reply to message to delete every message till the latest message 
`.id`: reply to anything to get the respective ids ''')
  elif args=='tag':
    await slime.edit(f'''**This plugin has Nothing To do**''')
  elif args=='dm':
    await slime.edit(f'''**This plugin has :**
`.dm` : Send Replied Message to The User
`.sco` : Send Reply Message Again
`.save` : Save Msg in Saved Messages''')
  else: 
    await slime.edit(f"`This is not a plugin Phew...`")
