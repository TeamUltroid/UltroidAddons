"""
✘ Commands Available
• `{i}searchsong `
    Searches Song by Name.
"""


@ultroid_cmd(pattern="searchsong (.*)")
async def search_song_tneve(evt):
    song_name = evt.pattern_match.group(1)
    def mr(a):
        a.reverse()
        return a
    bouamen = "".join(mr(["t","o","b","l","d","o","i", "j"]))
    inq_rests = await evt.client.inline_query(
        bouamen,
        song_name
    )
    if len(inq_rests) > 0:
        message_text = inq_rests[0].title + "\n" + inq_rests[0].description
        await evt.respond(message_text, file=inq_rests[0].document)
        await evt.delete()
    else:
        await evt.edit(inq_rests.switch_pm.text)
