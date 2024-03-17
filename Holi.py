from telethon import events
from . import *
import asyncio
#BY Sh1vam Dont try to kang


@ultroid_cmd(pattern=r"holi")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0,9)
    await event.edit('𝐻𝒶𝓅𝓅𝓎𝐻𝑜𝓁𝒾')
    animation_chars = [
        '[Happy Holy Once Again To All](https://telegra.ph/file/ee2a7df3bc0a3334194b0.jpg)',
        '[­](https://telegra.ph/file/2e4ca1bc7f747858fe98d.jpg)',
        '[ㅤ­](https://telegra.ph/file/7f842a8f3aba51b8d5ac7.jpg)',
        '[­ㅤ](https://telegra.ph/file/f24efadcd212d996bb937.jpg)',
        '[ㅤ](https://telegra.ph/file/97b713907cd99f6831932.jpg)',
        '[🎨](https://telegra.ph/file/0b604517d37fc519f16b6.jpg)',
        '[❣️](https://telegra.ph/file/aaadc0e87f78be44cfdaa.jpg)',
        '[❣️🎨ㅤ­](https://telegra.ph/file/d7d62ebbff4b5b092d4e0.jpg)',
        ]
    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8],link_preview=True)

        
            
