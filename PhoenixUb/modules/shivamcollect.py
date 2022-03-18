from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio

chat=-1001315396403
@phoenixub.on(events.NewMessage(chats=chat))
async def hi(event):
    if event.photo:
        a=event.media
        b=event.text
        if 'Latest_Movies_And_Series' in b:
            b=b.replace('Latest_Movies_And_Series','Newest_Movies_And_Series')
        else:
            b=b
        await ultroid.send_file(-1001675262116,a,caption=str(b))
    elif event.video:
        a=event.media
        b=event.text
        if 'Latest_Movies_And_Series' in b:
            b=b.replace('Latest_Movies_And_Series','Newest_Movies_And_Series')
        else:
            b=b
        await ultroid.send_file(-1001675262116,a,caption=str(b))
    elif event.sticker:
        await ultroid.send_file(-1001675262116,event.message)
