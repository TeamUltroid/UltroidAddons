from pyUltroid.dB.core import *
from rextester_py import rexec_aio
from support import *
from telethon import events
from rextester_py.rextester_aio import UnknownLanguage

#By @ProgrammingError
@tgbot.on(events.InlineQuery(pattern=r"rex (.*)"))
async def teamultroid(event: events.InlineQuery.Event):
    builder = event.builder
    bot = await tgbot.get_me()
    botuname = bot.username
    if event.query.user_id in sed:

        try:
            omk = event.text.split(' ', maxsplit=1)[1]
            if omk is not None:
                if "|" in omk:
                    lang, code = omk.split("|")
                else:
                    lang = "python 3"
                    code = omk
                output = await rexec_aio(lang, code)
                stats = output.stats
                if output.errors is not None:
                    outputt = output.errors
                    resultm = builder.article(
                        title="Code",
                        description=f"Language-`{lang}` & Code-`{code}`",
                        text=f"Language:\n`{lang}`\n\nCode:\n`{code}`\n\nErrors:\n`{outputt}`\n\nStats:\n`{stats}`",
                    )
                else:#By @ProgrammingError
                    outputt = output.results
                    resultm = builder.article(
                        title="Code",#By @ProgrammingError
                        description=f"Language-`{lang}` & Code-`{code}`",
                        text=f"Language:\n`{lang}`\n\nCode:\n`{code}`\n\nResult:\n`{outputt}`\n\nStats:\n`{stats}`",
                    )
                await event.answer([resultm])
        except UnknownLanguage:
            resultm = builder.article(
                title="Error",#By @ProgrammingError
                description="Invalid language choosen",
                text="The list of valid languages are\n\nc#, vb.net, f#, java, python, c (gcc), \nc++ (gcc), php, pascal, objective-c, haskell, \nruby, perl, lua, nasm, sql server, javascript, lisp, prolog, go, scala, \nscheme, node.js, python 3, octave, c (clang), \nc++ (clang), c++ (vc++), c (vc), d, r, tcl, mysql, postgresql, oracle, swift, \nbash, ada, erlang, elixir, ocaml, \nkotlin, brainfuck, fortran",
            )
            await event.answer([resultm])
    else:
        return#By @ProgrammingError

@inline
async def omkkkk(event):
    builder = event.builder
    query = event.text
    if event.query.user_id in sed and query.startswith("rtlangs"):
      resultm = builder.article(
          title="Code",
          description="Languages",
          text="c#, vb.net, f#, java, python, c (gcc), \nc++ (gcc), php, pascal, objective-c, haskell, \nruby, perl, lua, nasm, sql server, javascript, lisp, prolog, go, scala, \nscheme, node.js, python 3, octave, c (clang), \nc++ (clang), c++ (vc++), c (vc), d, r, tcl, mysql, postgresql, oracle, swift, \nbash, ada, erlang, elixir, ocaml, \nkotlin, brainfuck, fortran",
      )
      await event.answer([resultm])
