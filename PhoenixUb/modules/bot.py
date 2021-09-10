from PhoenixUb import phoenixub, phoenix, mention, alive_pic, help_strings
from telethon import events, Button
from datetime import datetime as dt

@phoenixub.on(events.NewMessage(outgoing=True, pattern=r'^#(alive)'))
async def alive(slime):
  me = await phoenixub.get_me()
  date = dt.now()
  date = date.strftime("%B %d, %Y")
  kek = mention(me.first_name, me.id)
  await slime.edit(f"「 **Great Sage On!** 」\n**Date:** `{date}`[­ ]({alive_pic})\n**Master:** {kek}", link_preview=True)
  
@phoenixub.on(events.NewMessage(outgoing=True, pattern=r'^#ping$'))
async def ping(slime):
  start = dt.now()
  await slime.edit("`۞pinging....`")
  end = dt.now()
  pon = (start - end).microseconds / 1000
  await slime.edit(f"ᑭOᑎᘜ!!\n\npong time: {pon}ms")

@phoenix.on(events.NewMessage(incoming=True,pattern=r'^\/start'))
async def start(slime):
  if slime.message.text != '/start':
    query = slime.message.text.split(' ', 1)[1]
    if query == 'help':
      await slime.reply(help_strings)
      return
    else:
      pass
  bot = await phoenix.get_me()
  user = await phoenixub.get_me()
  text = f'Im {bot.first_name} a great sage, and helper for {user.first_name}'
  await slime.reply(text)

  
@phoenix.on(events.InlineQuery(pattern=r'help'))
async def helppp(slime):
  builder = slime.builder 
  bot = await phoenix.get_me()
  phoenix_name = bot.username
  h = [
    builder.article(
    title='Help',
    text='Press button, to see help',
    buttons=[
      Button.url(
        text='Help',
        url=f'https://t.me/{phoenix_name}?start=help',
        )
      ]
  )
  ]
  await slime.answer(h)

@phoenix.on(events.CallbackQuery(pattern=b'help'))
async def helpcall(slime):
  await slime.answer(help_strings, alert=True)
  
@phoenixub.on(events.NewMessage(outgoing=True,pattern=r'^#help$'))  
async def helpp(slime):
  bot = await phoenix.get_me()
  great_sage = bot.username
  results = await phoenix.inline_query(great_sage, "help") 
  await results[0].click(slime.chat_id, reply_to=slime.reply_to_msg_id, hide_via=True) 
