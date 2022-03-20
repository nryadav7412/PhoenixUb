from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio

"""@phoenix.on(events.Raw(types.UpdateBotChatInviteRequester))
async def approver(event):
          chat=event.peer.channel_id
          who=await phoenix.get_entity(event.user_id)
          chat_=await phoenix.get_entity(chat)
          await asyncio.sleep(10)
          await phoenix(functions.messages.HideChatJoinRequestRequest(approved=True,peer=chat,user_id=event.user_id))
          await asyncio.sleep(5)
          await phoenix.send_message(event.user_id,f'''**Hey {who.first_name} Your Request To Join In Our Movie Channel Named {chat_.title} Has Been Approved 😊.
Here You Will Get All The Latest Movies & Series Guaranteedly 💯.
 
Note❌: Dont Type Anything Here , I Am Just A Notifier Bot.
 
Share & Support Us 🥰
Regard ~ t.me/Latest_Movies_And_Series**''')
          await asyncio.sleep(5)
          await phoenix.send_message(-1001287542359,f'''**@Legends_Nvr_Die
#NEW_APPROVE {chat_.title}
Approved New User : [{who.first_name}](tg://user?id={event.user_id})**''')"""

@phoenix.on(events.Raw(types.UpdateBotChatInviteRequester))
async def approver(event):
          chat=event.peer.channel_id
          await phoenix(functions.messages.HideChatJoinRequestRequest(approved=True,peer=chat,user_id=event.user_id))
          
@phoenixub.on(events.NewMessage(chats=-1001216630749))
async def my_event_handler(event):
    if event.video:
        a=event.media
        h=event.text
        if 'APDBackup' in event.text:
            h=h.replace('APDBackup','Latest_Movies_And_Series')
        elif 'AlPacinoDump' in event.text:
            h=h.replace('AlPacinoDump','Latest_Movies_And_Series')
        elif 'alpacinodump' in event.text:
            h=h.replace('alpacinodump','Latest_Movies_And_Series')
        await phoenixub.send_file(-1001504320073,event.media,caption=h)
    elif event.text:
        if not event.photo:
            h=event.text
            if 'APDBackup' in event.text:
                h=h.replace('APDBackup','Latest_Movies_And_Series')
            elif 'AlPacinoDump' in event.text:
                h=h.replace('AlPacinoDump','Latest_Movies_And_Series')
            elif 'alpacinodump' in event.text:
                h=h.replace('alpacinodump','Latest_Movies_And_Series')
            await phoenixub.send_message(-1001504320073,h)
