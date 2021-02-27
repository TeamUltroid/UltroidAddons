import random
import re


UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "ult",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

@ultroid_cmd( pattern="owo(?: |$)(.*)")
async def faces(ult):
    """ UwU """
    if not ult.text[0].isalpha() and ult.text[0] not in ("/", "#", "@", "!"):
        textx = await ult.get_reply_message()
        message = ult.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await ult.edit("` UwU no text given! `")
            return

        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"(R|L)", "W", reply_text)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(UWUS), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text += " " + random.choice(UWUS)
        await ult.edit(reply_text)