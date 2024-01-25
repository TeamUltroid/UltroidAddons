# Creator - @THE_BL_ACK_HAT @Shivam_Patel
#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}pokemon <query>`
    Send details of Pokemon.

• `{i}pokecard <query>`
    Send Card of Pokemon.
"""

import aiohttp
from pokedex import pokedex as badhiya
from . import ultroid_cmd, async_searcher


@ultroid_cmd(pattern="pokemon ?(.*)")
async def pokedex(event):
    input_param = event.pattern_match.group(1).lower()

    # Check if the input is numeric or a string
    if input_param.isdigit():
        # If numeric, treat it as a Pokémon number
        url = f"https://pokeapi.co/api/v2/pokemon/{input_param}"
    else:
        # If a string, treat it as a Pokémon name
        url = f"https://pokeapi.co/api/v2/pokemon/{input_param.lower()}"

    xx = await event.eor("`Booting up the Pokédex........`")

    # Get Pokemon details
    try:
        result = await async_searcher(url, re_json=True)
        species_result = await async_searcher(f"https://pokeapi.co/api/v2/pokemon-species/{input_param}", re_json=True)
    except KeyError:
        await event.eor("`Error getting Pokémon details. Please check the input or make sure the Pokémon exists in the Pokédex.`")
        return
    except aiohttp.client_exceptions.ContentTypeError:
        await event.eor("`Pokémon not found in the Pokédex.`")
        return

    try:
        name = result["name"]
        types = [type_info["type"]["name"]
                 for type_info in result.get("types", [])]
        abilities = [ability_info["ability"]["name"]
                     for ability_info in result.get("abilities", [])]
        # Convert height from decimeters to meters
        height = result.get("height", "Not available") / 10
        # Convert weight from hectograms to kilograms
        weight = result.get("weight", "Not available") / 10
        stats = result.get("stats", [])
        moves = result.get("moves", [])
        description = species_result.get(
            "flavor_text_entries", [])[0].get(
            "flavor_text", "Not available")
        sprite_url = result.get("sprites", {}).get("front_default")
    except KeyError:
        await event.eor("`Error getting Pokémon details. Please check the input.`")
        return

    # Additional details
    evolution_line = "None"
    generation = "Not available"

    # Check if species_result is not None and contains necessary properties
    if species_result and species_result.get(
            "evolves_from_species") and "name" in species_result["evolves_from_species"]:
        evolution_line = species_result["evolves_from_species"]["name"]

    # Get generation information
    if species_result and "generation" in species_result:
        generation_url = species_result["generation"]["url"]
        generation_result = await async_searcher(generation_url, re_json=True)
        generation = generation_result.get("name", "Not available")

    # Prepare moves
    move_names = [move_info["move"]["name"]
                  for move_info in moves[:7]]  # Get the first 7 moves

    while len(move_names) < 7:
        move_names.append("Not available")

    # Prepare stats
    stat_values = {stat["stat"]["name"]: stat["base_stat"] for stat in stats}

    # Prepare abilities
    abilities_str = ", ".join(abilities) if abilities else "Not available"

    # Get weaknesses using the additional API request
    lol = await async_searcher(f"https://api.pokemontcg.io/v1/cards?name={name}", re_json=True)
    try:
        weaknesses = lol["cards"][0]["weaknesses"][0]["type"]
    except (KeyError, IndexError):
        weaknesses = "Not available"

    cap = f"""
**NAME** : `{name}`
**TYPE** : `{', '.join(types)}`
**SPECIES** : `{species_result.get("name", "Not available")}`
**Evolution Line** : `{evolution_line}`
**Generation** : `{generation}`
**ABILITIES** : `{abilities_str}`
**WEAKNESSES** : `{weaknesses}`
**WEIGHT** : `{weight}` kilograms
**HEIGHT** : `{height}` meters

**Stats**                               **Moves**
**Hp**      : `{stat_values.get('hp', "Not available")}`              `(1){move_names[0]}`
**Attack**  : `{stat_values.get('attack', "Not available")}`           `(2){move_names[1]}`
**Defense** : `{stat_values.get('defense', "Not available")}`         `(3){move_names[2]}`
**Sp_atk**  : `{stat_values.get('special-attack', "Not available")}`           `(4){move_names[3]}`
**Sp_def**  : `{stat_values.get('special-defense', "Not available")}`           `(5){move_names[4]}`
**Speed**   : `{stat_values.get('speed', "Not available")}`           `(6){move_names[5]}`
**Total**   : `{sum(stat_values.values())}`          `(7){move_names[6]}`
**DESCRIPTION** : `{description}`
"""

    # Send file and caption
    await event.client.send_file(event.chat_id, sprite_url, caption=cap)
    await xx.delete()


@ultroid_cmd(pattern="pokecard ?(.*)")
async def pokecard(event):
    pokename = event.pattern_match.group(1).lower()
    if not pokename:
        await event.eor("`Give A Pokemon name`")
        return
    rw = f"https://api.pokemontcg.io/v1/cards?name={pokename}"
    a = await async_searcher(rw, re_json=True)
    try:
        o = a["cards"][0]["imageUrlHiRes"]
        await event.client.send_file(
            await event.client.get_input_entity(event.chat_id), o
        )
        await event.delete()
    except BaseException:
        await event.eor("`Be sure To give correct Name`")
        return
