# Ultroid - UserBot
# Copyright (C) 2021-2025 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import get_help

__doc__ = get_help("help_converter")

import os
import time

from . import LOGS

try:
    import cv2
except ImportError:
    cv2 = None

try:
    from PIL import Image
except ImportError:
    LOGS.info(f"{__file__}: PIL  not Installed.")
    Image = None

from . import upload_file as uf

from . import (
    ULTConfig,
    bash,
    con,
    downloader,
    get_paste,
    get_string,
    udB,
    ultroid_cmd,
    uploader,
)

opn = []


@ultroid_cmd(
    pattern="thumbnail$",
)
async def _(e):
    r = await e.get_reply_message()
    if r.photo:
        dl = await r.download_media()
    elif r.document and r.document.thumbs:
        dl = await r.download_media(thumb=-1)
    else:
        return await e.eor("`Reply to Photo or media with thumb...`")
    nn = uf(dl)
    os.remove(dl)
    udB.set_key("CUSTOM_THUMBNAIL", str(nn))
    await bash(f"wget {nn} -O resources/extras/ultroid.jpg")
    await e.eor(get_string("cvt_6").format(nn), link_preview=False)


@ultroid_cmd(
    pattern="rename( (.*)|$)",
)
async def imak(event):
    reply = await event.get_reply_message()
    t = time.time()
    if not reply:
        return await event.eor(get_string("cvt_1"))
    inp = event.pattern_match.group(1).strip()
    if not inp:
        return await event.eor(get_string("cvt_2"))
    xx = await event.eor(get_string("com_1"))
    if reply.media:
        if hasattr(reply.media, "document"):
            file = reply.media.document
            image = await downloader(
                reply.file.name or str(time.time()),
                reply.media.document,
                xx,
                t,
                get_string("com_5"),
            )

            file = image.name
        else:
            file = await event.client.download_media(reply.media)
    if os.path.exists(inp):
        os.remove(inp)
    await bash(f'mv """{file}""" """{inp}"""')
    if not os.path.exists(inp) or os.path.exists(inp) and not os.path.getsize(inp):
        os.rename(file, inp)
    k = time.time()
    n_file, _ = await event.client.fast_uploader(
        inp, show_progress=True, event=event, message="Uploading...", to_delete=True
    )
    await event.reply(
        f"`{n_file.name}`",
        file=n_file,
        force_document=True,
        thumb=ULTConfig.thumb,
    )
    os.remove(inp)
    await xx.delete()


conv_keys = {
    "img": "png",
    "sticker": "webp",
    "webp": "webp",
    "image": "png",
    "webm": "webm",
    "gif": "gif",
    "json": "json",
    "tgs": "tgs",
}


@ultroid_cmd(
    pattern="convert( (.*)|$)",
)
async def uconverter(event):
    xx = await event.eor(get_string("com_1"))
    a = await event.get_reply_message()
    if a is None:
        return await event.eor("`Reply to Photo or media with thumb...`")
    input_ = event.pattern_match.group(1).strip()
    b = await a.download_media("resources/downloads/")
    if not b and (a.document and a.document.thumbs):
        b = await a.download_media(thumb=-1)
    if not b:
        return await xx.edit(get_string("cvt_3"))
    try:
        convert = conv_keys[input_]
    except KeyError:
        return await xx.edit(get_string("sts_3").format("gif/img/sticker/webm"))
    file = await con.convert(b, outname="ultroid", convert_to=convert)
    print(file)

    if file:
        await event.client.send_file(
            event.chat_id, file, reply_to=event.reply_to_msg_id or event.id
        )
        os.remove(file)
    else:
        await xx.edit("`Failed to convert`")
        return
    await xx.delete()

@ultroid_cmd(
    pattern="doc( (.*)|$)",
)
async def _(event):
    input_str = event.pattern_match.group(1).strip()
    if not (input_str and event.is_reply):
        return await event.eor(get_string("cvt_1"), time=5)
    xx = await event.eor(get_string("com_1"))
    a = await event.get_reply_message()
    if not a.message:
        return await xx.edit(get_string("ex_1"))
    with open(input_str, "w") as b:
        b.write(str(a.message))
    await xx.edit(f"**Packing into** `{input_str}`")
    await event.reply(file=input_str, thumb=ULTConfig.thumb)
    await xx.delete()
    os.remove(input_str)


@ultroid_cmd(
    pattern="open( (.*)|$)",
)
async def _(event):
    a = await event.get_reply_message()
    b = event.pattern_match.group(1).strip()
    if not ((a and a.media) or (b and os.path.exists(b))):
        return await event.eor(get_string("cvt_7"), time=5)
    xx = await event.eor(get_string("com_1"))
    rem = None
    if not b:
        b = await a.download_media()
        rem = True
    try:
        with open(b) as c:
            d = c.read()
    except UnicodeDecodeError:
        return await xx.eor(get_string("cvt_8"), time=5)
    try:
        await xx.edit(f"```{d}```")
    except BaseException:
        what, data = await get_paste(d)
        await xx.edit(
            f"**MESSAGE EXCEEDS TELEGRAM LIMITS**\n\nSo Pasted It On [SPACEBIN]({data['link']})"
        )
    if rem:
        os.remove(b)
