from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio

chat=-1001589866631
statuss=['Removed']

@phoenixub.on(events.NewMessage(chats=chat))
async def hi(event):
    if len(statuss)==0:
        if event.photo:
            a=event.media
            b=event.text
            if 'Latest_Movies_And_Series' in b:
                b=b.replace('Latest_Movies_And_Series','Newest_Movies_And_Series')
            else:
                b=b
            await phoenixub.send_file(-1001675262116,a,caption=str(b))
        elif event.video:
            a=event.media
            b=event.text
            if 'Latest_Movies_And_Series' in b:
                b=b.replace('Latest_Movies_And_Series','Newest_Movies_And_Series')
            else:
                b=b
            await phoenixub.send_file(-1001675262116,a,caption=str(b))
        elif event.sticker:
            await phoenixub.send_file(-1001675262116,event.message)
    else:
        pass
@phoenixub.on(events.NewMessage(outgoing=True,pattern='.rems'))
async def rems(event):
    if len(statuss)==0:
        statuss.append('Removed')
        print('Removed Connection With Shivam!')
        await event.edit('`Removed Connection With Shivam!`')
    else:
        await event.edit('`Already Removed Connection!`')
        
@phoenixub.on(events.NewMessage(outgoing=True,pattern='.adds'))
async def rems(event):
    if len(statuss)==1:
        statuss.pop()
        print('Added Connection With Shivam!')
        await event.edit('`Added Connection With Shivam!`')
    else:
        await event.edit('`Already Added Connection!`')
      
@phoenixub.on(events.NewMessage(outgoing=True,pattern='.name'))
async def name(event):
    if not event.reply:
        await event.edit(f'''`Please Reply To A Telegram File`''')
    if event.reply:
        a=await event.get_reply_message()
        if a.file:
            nm=a.file.name
            sz=a.file.size 
            zz=''
            if sz<=1024:
                zz+=str(sz)+' B'
            elif sz>1024 and sz<=1048576:
                zz+=str(round(sz/1024,2))+' KB'
            elif sz>1048576 and sz<=1073741824:
                zz+=str(round(sz/1048576,2))+' MB'
            else:
                zz+=str(round(sz/1073741824,2))+' GB'
 
            await event.edit(f'''**FileName** : `{nm}`
**FileSize** : `{zz}`''')
        else:
            await event.edit(f'''`Die Reply To A File`''')
    else:
        await event.edit(f'''`File Not Recognized`''')
