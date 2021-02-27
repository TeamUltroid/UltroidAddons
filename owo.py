#Made By @senkiu_ishigamiii FaceS Took From Google
"""
✘ Commands Available
• `{i}owo`
    Gives owo face (RePly to a msg)
"""

import random
import re
from . import HELP


uwus = [
    "(・`ω´・)",
    "UwU",
    "uwu",
    "OwO",
    "owo",
    "(●__●)",
    "(゜o゜;",
    "⊙.☉",
    "(ô_ô)",
    "~:o",
    "¶-¶",
    "(*^*)",
    "(•_•)",
    "(⑉⊙ȏ⊙)",
    "*(^O^)*",
    "(°_°)",
]

@ultroid_cmd( pattern="owo")
async def faces(ult):
    uff = random.choice(uwus)
    return await ult.edit(f"{uff}")
    
    
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
