import requests
from bs4 import BeautifulSoup

url = 'https://wowhead.com/'
cookies = dict(BCPermissionLevel='acceptAll')
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0", "Cookie": "cookieconsent=true"}, cookies=cookies)
content = html.content

soup = BeautifulSoup(content, 'html.parser')
allNewsDivs = soup.find_all("div", class_="news-post-header-title-group")
list = []
for div in soup.find_all("div", class_="news-post-header-title-group").find_all("a"):
    list.append(div)

print(list)