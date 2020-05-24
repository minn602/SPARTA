import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# css selector
# 순위 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# 제목 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# 가수 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for music in musics:
    artist_tag = music.select_one('td.info > a.artist.ellipsis')
    if artist_tag is not None:
        rank = music.find('td', {'class': 'number'}).contents[0].strip()
        title = music.select_one('td.info > a.title.ellipsis').text.lstrip()
        artist = artist_tag.text
        print(rank, title, artist)