from telethon import events, Button, types
from PhoenixUb import phoenixub 
import youtube_dl
import logging
import os
import ffmpeg 
from youtube_search import YoutubeSearch
from telethon.utils import get_attributes
import time

LOGS = logging.getLogger(__name__)


helper = '''

`.song <song>`: Get the Song From Youtube

'''

@phoenixub.on(events.NewMessage(outgoing=True,pattern=r'^.song(.*)'))
async def songs(slime):
  opts = {
    "outtmpl": "%(title)s.mp3",
    "logger": LOGS,
    "writethumbnail": True,
    "format": "bestaudio/best",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
  }
  args = slime.message.text[5:]
  if args.startswith("https://"):
    url = args
  else:
    result = YoutubeSearch(args,max_results=1).to_dict()
    url = "https://youtu.be/" + result[0]['id']
  await slime.edit('Finding Song....')
  time.sleep(4)
  print(url)
  with youtube_dl.YoutubeDL(opts) as ydl:
    info = ydl.extract_info(url, download=False)
    dl = ydl.prepare_filename(info)
    ydl.download([url])
  m = await slime.edit("Downloaded, Now uploading....")
  f = open(dl, 'rb')
  upload = await slime.client.upload_file(file=f)
  attributes, mime_type = get_attributes(str(dl))
  media = types.InputMediaUploadedDocument(
    file=upload,
    attributes=attributes,
    mime_type=mime_type,
    )
  async with phoenixub.action(slime.chat_id, 'audio'):
    await phoenixub.send_message(slime.chat_id, file=media, force_document=False)
  await m.delete()
  os.remove(dl)
