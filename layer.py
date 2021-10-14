import asyncio
import sys

from plugins import *


async def fetch():
    rd, wr = await asyncio.open_connection("raw.githubusercontent.com", 443, ssl=True)

    wr.write(
        b"GET /"
        + b"telegramdesktop/tdesktop/dev/Telegram/Resources/tl/api.tl"
        + b" HTTP/1.1\r\n"
        b"Host: raw.githubusercontent.com\r\n"
        b"\r\n"
    )
    await wr.drain()

    headers = await rd.readuntil(b"\r\n\r\n")
    if headers[-4:] != b"\r\n\r\n":
        raise ConnectionError("Connection closed")

    if not headers.startswith(b"HTTP/1.1 200 OK"):
        raise ValueError(
            "Bad status code: {}".format(headers[: headers.index(b"\r\n")])
        )

    index = headers.index(b"Content-Length:") + 16
    length = int(headers[index : headers.index(b"\r", index)])
    result = await rd.readexactly(length)

    wr.close()
    if sys.version_info >= (3, 7):
        await wr.wait_closed()

    return result


@ultroid_cmd(pattern="layer$")
async def layer(event):
    while True:
        mm = await event.client.send_message(
            int(udB.get("LOG_CHANNEL")), "`Checking For Layer Updates...`"
        )
        contents = await fetch()
        if str(hash(contents)) != udB.get("layer"):
            await mm.edit("`New Layer Update Available...`")
            with open("layer.txt", "w") as file:
                file.write(contents.decode())
            with open("layer.txt", "r") as file:
                version = (file.read()).split("\n")[-2].replace("// ", "")
            message = await event.client.send_file(
                int(udB.get("LOG_CHANNEL")),
                "layer.txt",
                caption=f"@karboncopy @buddhhu\n[{version} is available](https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/Resources/tl/api.tl)",
            )
            try:
                await message.pin()
            except BaseException:
                pass
            await mm.delete()
            udB.set("layer", str(hash(contents)))
        else:
            await mm.edit("`No Layer Updates Available.`")
        await asyncio.sleep(3 * 60 * 60)
