@ultroid_cmd(pattern="f (.*)")
async def f(ult):
    if not ult.text[0].isalpha() and ult.text[0] not in ("/", "#", "@", "!"):
        ff = ult.pattern_match.group(1)
        fff = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(ff*5, ff*1,ff*1, ff*4, ff*1, ff*1, ff*1)
        await ult.edit(fff)
