import random
hindi = ["Phatele Nirodh Ke Natije!","Chut Ka Maindak…","Abla Naari, Tere Bable Bhaari…","Chut Ke Pasine Mein Talay Hue Bhajiye…","Chullu Bhar Muth Mein Doob Mar!","Kaali Chut Ke Safed Jhaant…","Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain…","Naa Chut, Naa Choche, Aur Nakhre Noor Jahan Ke!","Teri Gaand Mein Kutte Ka Lund…","Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki French Beard Bana Doonga!"]
@ultroid_cmd(pattern="habuse")
async def coinflip(ult):
  await ult.edit("Typing...")
  h = random.choice(hindi)
  return await ult.edit(f"**{h}**")

english = ["You Look Like My Dick","Motherfucking Pubic Hair","You Are Your Neighbours Son","Asshole","Ants In Your Ass Motherdick","Butt Plug","You Are A Dickhead","Son Of a Hog","You Son Of A Bitch","Suck My Dick","You Sweat Of Lizards Cunt","DaughterFucker","You Are A Dirty Germ Of Loose Pussy","You Are Your Mothers Cunt","You Were Born With Mucus XD","Shut Up Whore!"]
@ultroid_cmd(pattern="eabuse")
async def coinflip(ult):
  await ult.edit("Typing...")
  e = random.choice(english)
  return await ult.edit(f"**{e}**")