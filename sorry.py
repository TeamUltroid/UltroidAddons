import random
sorry = ["I'm Sorry （｡≧ _ ≦｡）","≦(._.)≧ : Sorry","o(´д｀o) : I'm Sorry Pleaze Forgive me","Sorry ヾ(_ _*)","(๑•́ㅿ•̀๑ ) ᔆᵒʳʳᵞ","Sorry:(づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ","༒ᎦᎧᏒᏒⲨ☆ʝααи༒"]
@ultroid_cmd(pattern="sorry")
async def sorryy(ult):
  s = random.choice(sorry)
  return await ult.edit(f"{s}")