""" Sing a song... 
    Command .rflirth

    By @veryhelpful"""

import asyncio
import random

from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"rflirth$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("here a fact about you......")
    await asyncio.sleep(1)
    s = random.randrange(1, 8)
    if s == 1:
        await event.edit(
            "Doctor Ne Advice Kia Hai Ki Sone Se Pahle Apki Pic Dekh Kar Sona Jaroori Hai, Warna Heart Attack Aa Sakta Hai."
        )
    if s == 2:
        await event.edit(
            "Ap Itne Cute Ho Ki Agar Mai Msg Na Bhi Karna Chahu.To Bhi Mera Hath Khud Keypad Pr Chalne Lagta Hai."
        )
    if s == 3:
        await event.edit(
            "Aag joh dil mein lagi hai, usse duniya mein laga doonga main ... joh teri doli uthi, zamaane ko jalaa doonga main"
        )
    if s == 4:
        await event.edit(
            "Jaldi se koi bhagwan ko bulao kyuki ek pari kho gayi hain aur wo pari yaha mujhse chatting kar rahi hain."
        )
    if s == 5:
        await event.edit(
            "Meri aankho ko kuch ho gaya hain, aap per se hat hi nahi rahi hain"
        )
    if s == 6:
        await event.edit(
            "Aap choro ke raja lagte ho kyuki aapne mera dil chura liya hain"
        )
    if s == 7:
        await event.edit(
            "Aapki aankhe ocean ki tarah blue he aur me usme har baar dub jata hu"
        )
    if s == 8:
        await event.edit(
            "Aap ek camera ki tarah ho jab bhi aapka photos dekhta hu meri automatic smile aaa jati hain"
        )
