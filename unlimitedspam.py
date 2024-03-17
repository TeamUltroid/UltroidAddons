from . import *

@ultroid_cmd(pattern="uspam")
async def unlimitedspam(ult):
    input = ult.text[7:]
    udB.delete("USPAM")
    x = None
    while x == None:
        x = Redis("USPAM")
        await ult.respond(input)


@ultroid_cmd(pattern="stopuspam$")
async def _(e):
    udB.set("USPAM", ".")
    await eod(e, "Unlimited spam stopped")