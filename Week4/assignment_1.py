import urllib.request
from bs4 import BeautifulSoup

# url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_252085.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

num_sum = 0
for tag in tags:
	num_sum += int(tag.contents[0])

print(num_sum)
