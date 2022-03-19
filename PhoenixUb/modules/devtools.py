from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio
import io
import os
import sys
import traceback

@phoenixub.on(event.NewMessage(outgoing=True , pattern=".eval "))
