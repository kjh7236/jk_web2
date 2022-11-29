import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=TlJGrd24w-c'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
video_id = url.split('=')[1]

title = soup.select_one('title').text
img = 'https://img.youtube.com/vi/'+video_id+'/0.jpg'
