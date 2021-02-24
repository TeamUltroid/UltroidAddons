# Plugin for ur gf
# Code by @maxprogrammer007 (orginally by @H1M4N5HU0P )for @theultroid
# Ported for Ultroid < https://github.com/TeamUltroid/Ultroid >   
# Type .iloveyou to see the love.

"""
✘ Commands Available -
• `{i}iloveyou`
    Show your love.
"""

import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="iloveyou$"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("""❤❤❤❤❤❤❤❤
❤❤❤❤❤❤❤❤
             ❤❤❤
             ❤❤❤
             ❤❤❤
             ❤❤❤
             ❤❤❤
             ❤❤❤
             ❤❤❤
             ❤❤❤ 
             ❤❤❤
❤❤❤❤❤❤❤❤
❤❤❤❤❤❤❤❤\n

❤❤
❤❤
❤❤
❤❤
❤❤
❤❤
❤❤
❤❤
❤❤❤❤❤❤❤❤
❤❤❤❤❤❤❤❤\n

⁭
           ❤❤❤❤❤
      ❤❤❤❤❤❤❤
   ❤❤                       ❤❤
 ❤❤                          ❤❤
❤❤                            ❤❤
❤❤                            ❤❤
 ❤❤                           ❤❤
   ❤❤                       ❤❤
       ❤❤❤❤❤❤❤
            ❤❤❤❤❤\n

⁭
❤❤                              ❤❤
  ❤❤                          ❤❤
    ❤❤                      ❤❤
      ❤❤                  ❤❤
         ❤❤             ❤❤
           ❤❤         ❤❤
             ❤❤     ❤❤
               ❤❤ ❤❤
                  ❤❤❤
                       ❤\n

⁭
❤❤❤❤❤❤❤❤
❤❤❤❤❤❤❤❤
❤❤
❤❤
❤❤❤❤❤❤
❤❤❤❤❤❤
❤❤
❤❤
❤❤❤❤❤❤❤❤
❤❤❤❤❤❤❤❤\n


❤❤                         ❤❤
  ❤❤                    ❤❤
     ❤❤              ❤❤
        ❤❤        ❤❤
           ❤❤  ❤❤
              ❤❤❤
                ❤❤
                ❤❤
                ❤❤
                ❤❤
                ❤❤\n

⁭
        ❤❤❤❤❤❤
     ❤❤❤❤❤❤❤
   ❤❤                     ❤❤
 ❤❤                         ❤❤
❤❤                           ❤❤
❤❤                           ❤❤
 ❤❤                         ❤❤
   ❤❤                     ❤❤
      ❤❤❤❤❤❤❤
            ❤❤❤❤❤\n

⁭
❤❤                      ❤❤
❤❤                      ❤❤
❤❤                      ❤❤
❤❤                      ❤❤
❤❤                      ❤❤
❤❤                      ❤❤
❤❤                      ❤❤
  ❤❤                  ❤❤
      ❤❤❤❤❤❤
            ❤❤❤❤""")


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
