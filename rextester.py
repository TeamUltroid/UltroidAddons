#    ultroid - userbot
#    Copyright (C) 2021 Ultroid

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# by @its_xditya


"""
✘ Commands Available -

• `{i}rex <lang code> <code> -`
   `Run code of any Language on telegram.`

"""

from rextester_py import rexec

from . import *


@ultroid_cmd(pattern="rex")
async def _(event):
    x = await eor(event,"Processing ...")
    evtxt = event.text.split(" ", maxsplit=1)[1]
    try:
        lang = evtxt.split("//", maxsplit=1)[0]
        cmd = evtxt.split("//", maxsplit=1)[1]
    except BaseException:
        return await eor(event,
            f"Syntax - \n`{Var.HNDLR}rex language//code`\nLanguages can be found [here](https://github.com/nitanmarcel/rextester_py#languages)."
        )
    try:
        res = rexec(lang, cmd, None).results
        err = rexec(lang, cmd, None).errors
        wrns = rexec(lang, cmd, None).warnings
        # statt = rexec(lang, cmd, None).stats
    except Exception as e:
        if str(e) == "Unknown language":
            return await x.edit(
                "ERROR:\n`Unknown Language!!\nCheck available languages `[here](https://github.com/nitanmarcel/rextester_py#languages)"
            )
        return await x.edit(f"ERROR:**\n`{str(e)}`")
    out = f"- Rextester**\n\n**Language: `{lang}`\n**Code: `{cmd}\n\n**Output:** {res}`\n\n"
    if err is not None:
        out += f"Error: `{err}`\n\n"
    if wrns is not None:
        out += f"Warnings: `{wrns}`\n\n"
    # reducing time taken...
    # out += f"Stats: {statt}"
    await x.edit(out)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
