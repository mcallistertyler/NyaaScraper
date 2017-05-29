import requests
import os
import errno
from bs4 import BeautifulSoup
path = "/Torrents/"
os.makedirs(os.path.dirname(path), exist_ok=True)
def download(url, file_name):
	with open(path + file_name.replace('\n', '') + '.torrent', "wb") as file:
		#get request
		response = requests.get(url)
		file.write(response.content)

page = requests.get("https://nyaa.pantsu.cat")
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find('div', id='content')
names = content.find_all(class_='tr-name home-td')

torrents = content.find_all('a', title='Torrent file')
#print(content)
for x in range(0, len(torrents)):
	file_name = names[x].get_text()
	torrentURL = torrents[x]['href']
	download(torrentURL, file_name)