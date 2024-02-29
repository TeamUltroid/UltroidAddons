import random
coin = ['Head','Tail']
@ultroid_cmd(pattern="coinflip")
async def coinflip(ult):
  await ult.edit("Tossing coin...")
  c = random.choice(coin)
  return await ult.edit(f"**Result :** {c}")
  #credit to @Arnab431 and @senku_ishigamiii