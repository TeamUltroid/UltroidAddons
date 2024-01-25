# Ported From DarkCobra Originally By UNIBORG
# Fixed by @TrueSaiyan
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}speedtst` Displays in Text
    Test Your Server Speed.

• `{i}speedtest Displays in Image
    Test Your Server Speed.
"""

from datetime import datetime

import speedtest

from . import *


@nimbus_cmd(pattern="speedtst ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    as_document = None
    if input_str == "file":
        as_document = True
    elif input_str == "image":
        as_document = False
    xx = await event.eor("`Calculating Nimbus Server Speed. Please wait!`")
    start = datetime.now()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    end = datetime.now()
    ms = (end - start).seconds
    response = s.results.dict()
    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:
        response = s.results.share()
        speedtest_image = response
        if as_document is None:
            await xx.edit(
                """`Nimbus Server Speed in {} sec`

`Download: {}`
`Upload: {}`
`Ping: {}`
`Internet Service Provider: {}`
`ISP Rating: {}`""".format(
                    ms,
                    humanbytes(download_speed),
                    humanbytes(upload_speed),
                    ping_time,
                    i_s_p,
                    i_s_p_rating,
                )
            )
        else:
            await event.client.send_file(
                event.chat_id,
                speedtest_image,
                caption=f"**SpeedTest** completed in {ms} seconds",
                force_document=as_document,
                reply_to=reply_msg_id,
                allow_cache=False,
            )
            await event.delete()
    except Exception as exc:  # dc
        await xx.edit(
            """**SpeedTest** completed in {} seconds
Download: {}
Upload: {}
Ping: {}


__With the Following ERRORs__
{}""".format(
                ms,
                humanbytes(download_speed),
                humanbytes(upload_speed),
                ping_time,
                str(exc),
            )
        )


temxt = (
    "**Nimbus Speedtest completed in {0} seconds.**\n\n"
    "**Download:**  `{1}` \n"
    "**Upload:**  `{2}` \n"
    "**Ping:**  `{3} ms` \n"
    "**Internet Provider:**  `{4} ({5})` \n"
)


@nimbus_cmd(pattern="speedtest ?(.*)")
async def speemdtest(event):
    args = event.pattern_match.group(1)
    xx = await eor(event, "`Calculating Nimbus Server Speed. Please wait!``")
    start = datetime.now()
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()  # dchehe
    end = datetime.now()
    ms = (end - start).seconds
    response = s.results.dict()

    download_speed = response.get("download")
    upload_speed = response.get("upload")
    ping_time = response.get("ping")
    client_infos = response.get("client")
    i_s_p = client_infos.get("isp")
    i_s_p_rating = client_infos.get("isprating")

    if args and args == "text":
        await xx.edit(temxt.format(
            ms,
            convert_from_bytes(download_speed),
            convert_from_bytes(upload_speed),
            ping_time,
            i_s_p,
            i_s_p_rating,
        ))
    else:
        try:
            speedtest_image = s.results.share()
            await event.client.send_file(
                event.chat_id,
                speedtest_image,  # heeehe
                caption="**SpeedTest** completed in {} seconds".format(ms),
                force_document=False,
                reply_to=event.reply_to_msg_id,
                allow_cache=False
            )
            await xx.delete()
        except Exception as exc:  # dc
            xx2 = temxt.format(
                ms,
                convert_from_bytes(download_speed),
                convert_from_bytes(upload_speed),
                ping_time,
                i_s_p,
                i_s_p_rating,
            )
            return await xx.edit(
                f"{xx2} \n**Exception:** `{exc}`"
            )


def convert_from_bytes(size):
    power = 2 ** 10
    n = 0
    units = {
        0: "",
        1: "Kilobytes/s",
        2: "Megabytes/s",
        3: "Gigabytes/s",
        4: "Terabytes/s"}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"
