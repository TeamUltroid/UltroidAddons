import asyncio

@ultroid_cmd(pattern="clappp")
async def clap(ult):
  await ult.edit("👐👏👐👏 👐👏")
  await asyncio.sleep(1)
  await ult.edit("👐👏👐👏👐👏👐")