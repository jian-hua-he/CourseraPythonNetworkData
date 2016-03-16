import urllib.request
from bs4 import BeautifulSoup

# Sample url
# url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'

# Actual url
# url = 'http://python-data.dr-chuck.net/known_by_Honour.html'

url = input('Enter url:')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

for i in range(0, count + 1, 1):
	print('Retrieving: ' + url)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	url = tags[position - 1].get('href')
