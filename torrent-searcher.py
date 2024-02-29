"""
Torrent Search Plugin for Userbot. //torrentdownloads.me
cmd: .search search_string
Note: Number of results are currently limited to 11
By:-@Zero_cool7870

"""
from bs4 import BeautifulSoup as bs 
import requests, asyncio, json

def dogbin(magnets):
	counter = 0
	urls = []
	while counter != len(magnets):
		message = magnets[counter]
		url = "https://nekobin.com/api/documents"
		r = requests.post(url, json={"content": message}).json().get("result").get("key")
		url = f"https://nekobin.com/raw/{r}"
		urls.append(url)
		counter = counter + 1
	return urls	
	
@ultroid_cmd(pattern="torsearch ?(.*)")
async def tor_search(event):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
	search_str = event.pattern_match.group(1)
	a = await eor(event, "Searching for "+search_str+".....")
	if " " in search_str:
		search_str = search_str.replace(" ","+")
		res = requests.get("https://www.torrentdownloads.me/search/?new=1&s_cat=0&search="+search_str,headers)
	else:
		res = requests.get("https://www.torrentdownloads.me/search/?search="+search_str,headers)
	source = bs(res.text,'lxml')
	urls = []
	magnets = []
	titles = []
	counter = 0
	for div in source.find_all('div',{'class':'grey_bar3 back_none'}):
		try:
			title = div.p.a['title']
			title = title[20:]
			titles.append(title)
			urls.append("https://www.torrentdownloads.me"+div.p.a['href'])
		except KeyError:
			pass
		except TypeError:
			pass
		except AttributeError:
			pass	
		if counter == 11:
			break		
		counter = counter + 1
	if not urls:
		return await a.edit("Either the Keyword was restricted or not found..")
	for url in urls:
		res = requests.get(url,headers)
		source = bs(res.text,'lxml')
		for div in source.find_all('div',{'class':'grey_bar1 back_none'}):
			try:
				mg = div.p.a['href']
				magnets.append(mg)
			except Exception as e:
				pass
	shorted_links = dogbin(magnets)
	msg = ""
	try:
		search_str = search_str.replace("+"," ")
	except:
		pass	
	msg = "**Torrent Search Query**\n`{}`".format(search_str)+"\n**Results**\n"
	counter = 0
	while counter != len(titles):
		msg = msg + "⁍ [{}]".format(titles[counter])+"({})".format(shorted_links[counter])+"\n\n"
		counter = counter + 1
	await a.edit(msg,link_preview=False)