#    Ultroid - UserBot
#    Copyright 2020 (c)

# For song and vsong
#    Thanks to @AvinashReddy for the ytdl base and @xditya
# Lyrics ported from Dark Cobra
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


"""
✘ Commands Available -
• `{i}song <search query>`
    upload song as mp3.

• `{i}vsong <search query>`
    upload video songs.

• `{i}lyrics <search query>`
    get lyrics of song.

• `{i}songs <search query>`
    alternative song command.
"""


import json
import os
import random
import time

from lyrics_extractor import SongLyrics as sl
from lyrics_extractor.lyrics import LyricScraperException as LyError
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import DocumentAttributeAudio
from telethon.tl.types import InputMessagesFilterMusic as filtermus
from youtube_dl import YoutubeDL
from youtube_dl.utils import (ContentTooShortError, DownloadError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from youtubesearchpython import SearchVideos

from . import *


@ultroid_cmd(pattern="song ?(.*)")
async def download_video(ult):
    a = ult.text
    if len(a) <= 5 and a[5] == "s":
        return
    x = await eor(ult, "Searching...")
    url = ult.pattern_match.group(1)
    if not url:
        return await x.edit("**Error**\nUsage - `.song <song name>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await x.edit("`No matching song found...`")
    type = "audio"
    await x.edit(f"`Preparing to download {url}...`")
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        await x.edit("`Getting info...`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await x.edit(f"`{str(DE)}`")
        return
    except ContentTooShortError:
        await x.edit("`The download content was too short.`")
        return
    except GeoRestrictedError:
        await x.edit(
            "`Video is not available from your geographic location due to"
            + " geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await x.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await x.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await x.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        return await x.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await x.edit("`There was an error during info extraction.`")
    except Exception as e:
        return await x.edit(f"{str(type(e)): {str(e)}}")
    dir = os.listdir()
    if f"{rip_data['id']}.mp3.jpg" in dir:
        thumb = f"{rip_data['id']}.mp3.jpg"
    elif f"{rip_data['id']}.mp3.webp" in dir:
        thumb = f"{rip_data['id']}.mp3.webp"
    else:
        thumb = None
    tail = time.time()
    ttt = await uploader(
        rip_data["id"] + ".mp3",
        rip_data["title"] + ".mp3",
        tail,
        x,
        "Uploading " + rip_data["title"],
    )
    CAPT = f"⫸ Song - {rip_data['title']}\n⫸ By - {rip_data['uploader']}\n"
    await ultroid_bot.send_file(
        ult.chat_id,
        ttt,
        thumb=thumb,
        supports_streaming=True,
        caption=CAPT,
        attributes=[
            DocumentAttributeAudio(
                duration=int(rip_data["duration"]),
                title=str(rip_data["title"]),
                performer=str(rip_data["uploader"]),
            )
        ],
    )
    await x.delete()
    os.remove(f"{rip_data['id']}.mp3")
    try:
        os.remove(thumb)
    except BaseException:
        pass


@ultroid_cmd(pattern="vsong (.*)")
async def download_vsong(ult):
    x = await eor(ult, "Processing..")
    url = ult.pattern_match.group(1)
    if not url:
        return await x.edit("**Error**\nUsage - `.vsong <song name>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await x.edit("`No matching songs found...`")
    type = "audio"
    await x.edit("`Preparing to download...`")
    if type == "audio":
        opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
    try:
        await x.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        return await x.edit(f"`{str(DE)}`")
    except ContentTooShortError:
        return await x.edit("`The download content was too short.`")
    except GeoRestrictedError:
        return await x.edit(
            "`Video is not available from your geographic location due to"
            + " geographic restrictions imposed by a website.`"
        )
    except MaxDownloadsReached:
        return await x.edit("`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await x.edit("`There was an error during post processing.`")
    except UnavailableVideoError:
        return await x.edit("`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await x.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await x.edit("`There was an error during info extraction.`")
    except Exception as e:
        return await x.edit(f"{str(type(e)): {str(e)}}")
    tail = time.time()
    ttt = await uploader(
        rip_data["id"] + ".mp4",
        rip_data["title"] + ".mp4",
        tail,
        x,
        "Uploading " + rip_data["title"],
    )
    CAPT = f"⫸ Song - {rip_data['title']}\n⫸ By - {rip_data['uploader']}\n"
    await ultroid_bot.send_file(
        ult.chat_id,
        ttt,
        supports_streaming=True,
        caption=CAPT,
    )
    os.remove(f"{rip_data['id']}.mp4")
    await x.delete()


@ultroid_cmd(pattern=r"lyrics ?(.*)")
async def original(event):
    if not event.pattern_match.group(1):
        return await eor(event, "give query to search.")
    noob = event.pattern_match.group(1)
    ab = await eor(event, "Getting lyrics..")
    dc = random.randrange(1, 3)
    if dc == 1:
        danish = "AIzaSyAyDBsY3WRtB5YPC6aB_w8JAy6ZdXNc6FU"
    if dc == 2:
        danish = "AIzaSyBF0zxLlYlPMp9xwMQqVKCQRq8DgdrLXsg"
    if dc == 3:
        danish = "AIzaSyDdOKnwnPwVIQ_lbH5sYE4FoXjAKIQV0DQ"
    extract_lyrics = sl(f"{danish}", "15b9fb6193efd5d90")
    try:
        sh1vm = extract_lyrics.get_lyrics(f"{noob}")
    except LyError:
        return await eod(event, "No Results Found")
    a7ul = sh1vm["lyrics"]
    await ultroid_bot.send_message(event.chat_id, a7ul, reply_to=event.reply_to_msg_id)
    await ab.delete()


@ultroid_cmd(pattern="songs ?(.*)")
async def _(event):

    try:
        await ultroid_bot(ImportChatInviteRequest("DdR2SUvJPBouSW4QlbJU4g"))
    except UserAlreadyParticipantError:
        pass
    except Exception:
        return await eor(
            event,
            "You need to join [this]"
            + "(https://t.me/joinchat/DdR2SUvJPBouSW4QlbJU4g)"
            + "group for this module to work.",
        )
    args = event.pattern_match.group(1)
    if not args:
        return await eor(event, "`Enter song name`")
    okla = await eor(event, "processing...")
    chat = -1001271479322
    current_chat = event.chat_id
    try:
        async for event in ultroid_bot.iter_messages(
            chat, search=args, limit=1, filter=filtermus
        ):
            await ultroid_bot.send_file(current_chat, event, caption=event.message)
        await okla.delete()
    except Exception:
        return await eor(event, "`Song not found.`")
