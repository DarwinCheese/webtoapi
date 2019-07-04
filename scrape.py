import requests

url = 'https://tweakers.net/'
response = requests.get(url)
html = response.content
print html