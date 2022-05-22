"""
✘ Commands Available

• `{i}figlet <text>`
    Make a text a figlet.
"""

import pyfiglet

from . import *

CMD_SET = {
    "slant": "slant",
    "3D": "3-d",
    "5line": "5lineoblique",
    "alpha": "alphabet",
    "banner": "banner3-D",
    "doh": "doh",
    "iso": "isometric1",
    "letters": "letters",
    "allig": "alligator",
    "dotm": "dotmatrix",
    "bubble": "bubble",
    "bulb": "bulbhead",
    "digi": "digital",
    "3x5": "3x5",
    "1943": "1943____",
    "4x4": "4x4_offr",
    "5x7": "5x7",
    "5x8": "5x8",
    "64f1": "64f1____",
    "6x10": "6x10",
    "6x9": "6x9",
    "zooloo": "a_zooloo",
    "acro": "acrobatic",
    "aveng": "advenger",
    "allig2": "alligator2",
    "aqua": "aquaplan",
    "arrows": "arrows",
    "asc": "asc_____",
    "ascii12": "ascii12",
    "ascii9": "ascii9",
    "ascii": "ascii___",
    "assalt": "assalt_m",
    "asslt": "asslt__m",
    "atc": "atc_____",
    "atcg": "atc_gran",
    "avatar": "avatar",
    "bm200": "b_m__200",
    "banner3": "banner3",
    "banner4": "banner4",
    "barb": "barbwire",
    "basic": "basic",
    "battles": "battle_s",
    "battlesh": "battlesh",
    "baz": "baz__bil",
    "beer": "beer_pub",
    "bell": "bell",
    "big": "big",
    "bigascii12": "bigascii12",
    "bigascii9": "bigascii9",
    "bigchief": "bigchief",
    "bigmono12": "bigmono12",
    "bigmono9": "bigmono9",
    "binary": "binary",
    "block": "block",
    "brite": "brite",
    "briteb": "briteb",
    "britebi": "britebi",
    "britei": "britei",
    "broadway": "broadway",
    "bubbles": "bubble__",
    "buble": "bubble_b",
    "bhead": "bulbhead",
    "c1": "c1______",
    "c2": "c2______",
    "cascii": "c_ascii_",
    "cconsen": "c_consen",
    "calgphy2": "calgphy2",
    "caligraphy": "caligraphy",
    "catwalk": "catwalk",
    "causin": "caus_in_",
    "char1": "char1___",
    "char2": "char2___",
    "char3": "char3___",
    "char4": "char4___",
    "charact1": "charact1",
    "charact2": "charact2",
    "charact3": "charact3",
    "charact4": "charact4",
    "charact5": "charact5",
    "charact6": "charact6",
    "characte": "characte",
    "charset": "charset_",
    "chartr": "chartr",
    "chartri": "chartri",
    "chunky": "chunky",
    "circle": "circle",
    "clb6x10": "clb6x10",
    "clb8x10": "clb8x10",
    "clb8x8": "clb8x8",
    "clr4x6": "clr4x6",
    "clr5x10": "clr5x10",
    "clr5x6": "clr5x6",
    "clr5x8": "clr5x8",
    "clr6x10": "clr6x10",
    "clr6x6": "clr6x6",
    "clr6x8": "clr6x8",
    "clr7x10": "clr7x10",
    "clr7x8": "clr7x8",
    "clr8x10": "clr8x10",
    "clr8x8": "clr8x8",
    "coilcop": "coil_cop",
    "coinstak": "coinstak",
    "colossal": "colossal",
    "comsen": "com_sen_",
    "computer": "computer",
    "contessa": "contessa",
    "contrast": "contrast",
    "convoy": "convoy__",
    "cosmic": "cosmic",
    "cosmike": "cosmike",
    "cour": "cour",
    "courb": "courb",
    "courbi": "courbi",
    "couri": "couri",
    "crawford": "crawford",
    "cricket": "cricket",
    "cursive": "cursive",
    "cyberlarge": "cyberlarge",
    "cybermedium": "cybermedium",
    "cybersmall": "cybersmall",
    "ddragon": "d_dragon",
    "dcsbfmo": "dcs_bfmo",
    "decimal": "decimal",
    "deepstr": "deep_str",
    "defleppard": "defleppard",
    "demo1": "demo_1__",
    "demo2": "demo_2__",
    "demom": "demo_m__",
    "devilish": "devilish",
    "diamond": "diamond",
    "doom": "doom",
    "double": "double",
    "drpepper": "drpepper",
    "druid": "druid___",
    "efist": "e__fist_",
    "ebbs1": "ebbs_1__",
    "ebbs2": "ebbs_2__",
    "eca": "eca_____",
    "eftichess": "eftichess",
    "eftifont": "eftifont",
    "eftipiti": "eftipiti",
    "eftirobot": "eftirobot",
    "eftitalic": "eftitalic",
    "eftiwall": "eftiwall",
    "eftiwater": "eftiwater",
    "emboss": "emboss",
    "emboss2": "emboss2",
    "epic": "epic",
    "etcrvs": "etcrvs__",
    "f15": "f15_____",
    "facesof": "faces_of",
    "fairmea": "fair_mea",
    "fairligh": "fairligh",
    "fantasy": "fantasy_",
    "fbr12": "fbr12___",
    "fbr1": "fbr1____",
    "fbr2": "fbr2____",
    "fbrstri": "fbr_stri",
    "fbrtilt": "fbr_tilt",
    "fender": "fender",
    "finalass": "finalass",
    "fireing": "fireing_",
    "flynsh": "flyn_sh",
    "fourtops": "fourtops",
    "fp1": "fp1_____",
    "fp2": "fp2_____",
    "fraktur": "fraktur",
    "funkydr": "funky_dr",
    "future": "future",
    "future1": "future_1",
    "future2": "future_2",
    "future3": "future_3",
    "future4": "future_4",
    "future5": "future_5",
    "future6": "future_6",
    "future7": "future_7",
    "future8": "future_8",
    "fuzzy": "fuzzy",
    "gauntlet": "gauntlet",
    "ghostbo": "ghost_bo",
    "goofy": "goofy",
    "gothic": "gothic",
    "gothics": "gothic__",
    "graceful": "graceful",
    "gradient": "gradient",
    "graffiti": "graffiti",
    "grandpr": "grand_pr",
    "greek": "greek",
    "greenbe": "green_be",
    "hades": "hades___",
    "heavyme": "heavy_me",
    "helv": "helv",
    "helvb": "helvb",
    "helvbi": "helvbi",
    "helvi": "helvi",
    "heroboti": "heroboti",
    "hex": "hex",
    "highnoo": "high_noo",
    "hills": "hills___",
    "holly": "hollywood",
    "homepak": "home_pak",
    "houseof": "house_of",
    "hypabal": "hypa_bal",
    "hyper": "hyper___",
    "incraw": "inc_raw_",
    "invita": "invita",
    "iso2": "isometric2",
    "iso3": "isometric3",
    "iso4": "isometric4",
    "italic": "italic",
    "italics": "italics_",
    "ivrit": "ivrit",
    "jazmine": "jazmine",
    "jerusalem": "jerusalem",
    "joust": "joust___",
    "ktk": "katakana",
    "kban": "kban",
    "kgamesi": "kgames_i",
    "kikstar": "kik_star",
    "krakout": "krak_out",
    "larry3d": "larry3d",
    "lazyjon": "lazy_jon",
    "lcd": "lcd",
    "lean": "lean",
    "letter": "letter",
    "letterr": "letter_",
    "letterw3": "letterw3",
    "lexible": "lexible_",
    "linux": "linux",
    "lockergnome": "lockergnome",
    "lower": "lower",
    "madnurs": "mad_nurs",
    "madrid": "madrid",
    "magicma": "magic_ma",
    "marquee": "marquee",
    "mastero": "master_o",
    "maxfour": "maxfour",
    "mayhemd": "mayhem_d",
    "mcg": "mcg_____",
    "migally": "mig_ally",
    "mike": "mike",
    "mini": "mini",
    "mirror": "mirror",
    "mnemonic": "mnemonic",
    "modern": "modern__",
    "mono12": "mono12",
    "mono9": "mono9",
    "morse": "morse",
    "moscow": "moscow",
    "mshebrew210": "mshebrew210",
    "nancyjf": "nancyj-fancy",
    "nancyju": "nancyj-underlined",
    "nancyj": "nancyj",
    "newasci": "new_asci",
    "nfi1": "nfi1____",
    "nipl": "nipples",
    "notieca": "notie_ca",
    "npn": "npn_____",
    "ntgreek": "ntgreek",
    "null": "null",
    "nvscript": "nvscript",
    "o8": "o8",
    "octal": "octal",
    "odellak": "odel_lak",
    "ogre": "ogre",
    "okbeer": "ok_beer_",
    "os2": "os2",
    "outrun": "outrun__",
    "pshm": "p_s_h_m_",
    "pskateb": "p_skateb",
    "pacospe": "pacos_pe",
    "pagga": "pagga",
    "panther": "panther_",
    "pawnins": "pawn_ins",
    "pawp": "pawp",
    "peaks": "peaks",
    "pebbles": "pebbles",
    "pepper": "pepper",
    "phonix": "phonix__",
    "platoon2": "platoon2",
    "platoon": "platoon_",
    "pod": "pod_____",
    "poison": "poison",
    "puffy": "puffy",
    "pyramid": "pyramid",
    "r2d2": "r2-d2___",
    "rad": "rad_____",
    "radphan": "rad_phan",
    "radical": "radical_",
    "rainbow": "rainbow_",
    "rallys2": "rally_s2",
    "rallysp": "rally_sp",
    "rampage": "rampage_",
    "rastan": "rastan__",
    "rawrecu": "raw_recu",
    "rci": "rci_____",
    "rectangles": "rectangles",
    "relief": "relief",
    "relief2": "relief2",
    "rev": "rev",
    "ripper": "ripper!_",
    "roadrai": "road_rai",
    "rockbox": "rockbox_",
    "rok": "rok_____",
    "roman": "roman",
    "romans": "roman___",
    "rot13": "rot13",
    "rounded": "rounded",
    "rowancap": "rowancap",
    "rozzo": "rozzo",
    "runic": "runic",
    "runyc": "runyc",
    "sans": "sans",
    "sansb": "sansb",
    "sansbi": "sansbi",
    "sansi": "sansi",
    "sblood": "sblood",
    "sbook": "sbook",
    "sbookb": "sbookb",
    "sbookbi": "sbookbi",
    "sbooki": "sbooki",
    "script": "script",
    "scripts": "script__",
    "serifcap": "serifcap",
    "shadow": "shadow",
    "shimrod": "shimrod",
    "short": "short",
    "skatero": "skate_ro",
    "skateord": "skateord",
    "skateroc": "skateroc",
    "sketchs": "sketch_s",
    "slide": "slide",
    "slscript": "slscript",
    "sm": "sm______",
    "small": "small",
    "smascii12": "smascii12",
    "smascii9": "smascii9",
    "smblock": "smblock",
    "smbraille": "smbraille",
    "smisome1": "smisome1",
    "smkeyboard": "smkeyboard",
    "smmono12": "smmono12",
    "smmono9": "smmono9",
    "smscript": "smscript",
    "smshadow": "smshadow",
    "smslant": "smslant",
    "smtengwar": "smtengwar",
    "spaceop": "space_op",
    "spcdemo": "spc_demo",
    "speed": "speed",
    "stacey": "stacey",
    "stampatello": "stampatello",
    "standard": "standard",
    "starwar": "star_war",
    "starwars": "starwars",
    "stealth": "stealth_",
    "stellar": "stellar",
    "stencil1": "stencil1",
    "stencil2": "stencil2",
    "stop": "stop",
    "straight": "straight",
    "street_s": "street_s",
    "subteran": "subteran",
    "superte": "super_te",
    "tofap": "t__of_ap",
    "tanja": "tanja",
    "tav1": "tav1____",
    "taxi": "taxi____",
    "tec1": "tec1____",
    "tec7000": "tec_7000",
    "tecrvs": "tecrvs__",
    "tengwar": "tengwar",
    "term": "term",
    "thick": "thick",
    "thin": "thin",
    "threepoint": "threepoint",
    "tipan": "ti_pan__",
    "ticks": "ticks",
    "ticksslant": "ticksslant",
    "tiles": "tiles",
    "times": "times",
    "timesofl": "timesofl",
    "tinkertoy": "tinker-toy",
    "tomahawk": "tomahawk",
    "tombstone": "tombstone",
    "top_duck": "top_duck",
    "trashman": "trashman",
    "trek": "trek",
    "triadst": "triad_st",
    "ts1": "ts1_____",
    "tsalagi": "tsalagi",
    "tsm": "tsm_____",
    "tsnbase": "tsn_base",
    "tty": "tty",
    "ttyb": "ttyb",
    "tubular": "tubular",
    "twincob": "twin_cob",
    "twopoint": "twopoint",
    "typeset": "type_set",
    "ucffan": "ucf_fan_",
    "ugalympi": "ugalympi",
    "unarmed": "unarmed_",
    "univers": "univers",
    "upper": "upper",
    "usa": "usa_____",
    "usapq": "usa_pq__",
    "usaflag": "usaflag",
    "utopia": "utopia",
    "utopiab": "utopiab",
    "utopiabi": "utopiabi",
    "utopiai": "utopiai",
    "vortron": "vortron_",
    "warofw": "war_of_w",
    "wavy": "wavy",
    "weird": "weird",
    "whimsy": "whimsy",
    "wideterm": "wideterm",
    "xbrite": "xbrite",
    "xbriteb": "xbriteb",
    "xbritebi": "xbritebi",
    "xbritei": "xbritei",
    "xchartr": "xchartr",
    "xchartri": "xchartri",
    "xcour": "xcour",
    "xcourb": "xcourb",
    "xcourbi": "xcourbi",
    "xcouri": "xcouri",
    "xhelv": "xhelv",
    "xhelvb": "xhelvb",
    "xhelvbi": "xhelvbi",
    "xhelvi": "xhelvi",
    "xsans": "xsans",
    "xsansb": "xsansb",
    "xsansbi": "xsansbi",
    "xsansi": "xsansi",
    "xsbook": "xsbook",
    "xsbookb": "xsbookb",
    "xsbookbi": "xsbookbi",
    "xsbooki": "xsbooki",
    "xtimes": "xtimes",
    "xtty": "xtty",
    "xttyb": "xttyb",
    "yiear": "yie-ar__",
    "yieark": "yie_ar_k",
    "zpilot": "z-pilot_",
    "zigzag": "zig_zag_",
    "zone7": "zone7___",
}

DataList = sorted(list(CMD_SET.values()))
Split = split_list(DataList, 25)
offset = 0

@ultroid_cmd(pattern="figlet( ?(.*)|$)")
async def figlet(event):
    input_str = event.pattern_match.group(1).strip()
    if not input_str:
        return await event.eor("`Provide some text to make figlet...`")
    if input_str == "list":
        global offset
        if offset == len(Split):
            offset = 0
        All = Split[offset]
        Text = "**List of Figlet Fonts :**\n\n"
        while All:
            c = 3
            Nline = "• " + " ".join(f"`{All[:3]}`")
            while (len(Nline) < 32):
                c += 1
                Nline += f" `{All[c]}`"
            Text += Nline + "\n"
            All = All[c:]
        await event.eor(Text)
        offset += 1
        return
    if "|" in input_str:
        text, cmd = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await event.eor("Please add some text to figlet")
        return
    if cmd is not None:
        try:
            font = CMD_SET[cmd]
        except KeyError:
            await event.eor("Invalid selected font.")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await event.eor(f"‌‌‎`{result}`")
