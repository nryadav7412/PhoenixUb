from PhoenixUb import phoenixub, phoenix
from telethon import events, Button, functions, types
import asyncio
import io
import os
import sys
import traceback

@phoenixub.on(event.NewMessage(outgoing=True , pattern=".eval ?(.*)"))
async def eval(event):
  cmd = "".join(event.message.message.split(maxsplit=1)[1:])
  if not cmd:
    await event.edit("`What should i run ?..`")
  catevent = await event.edit("`Running ...`")
  old_stderr = sys.stderr
  old_stdout = sys.stdout
  redirected_output = sys.stdout = io.StringIO()
  redirected_error = sys.stderr = io.StringIO()
  stdout, stderr, exc = None, None, None
  try:
      await aexec(cmd, event)
  except Exception:
      exc = traceback.format_exc()
  stdout = redirected_output.getvalue()
  stderr = redirected_error.getvalue()
  sys.stdout = old_stdout
  sys.stderr = old_stderr
  evaluation = ""
  if exc:
      evaluation = exc
  elif stderr:
      evaluation = stderr
  elif stdout:
      evaluation = stdout
  else:
      evaluation = "Success"
  final_output = (
        f"**•  Eval : **\n```{cmd}``` \n\n**•  Result : **\n```{evaluation}``` \n"
    )
  await event.edit(final_output)
