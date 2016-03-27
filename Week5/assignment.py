import urllib.request
import xml.etree.ElementTree as ET

# sample data url = 'http://python-data.dr-chuck.net/comments_42.xml'
# actual data url = 'http://python-data.dr-chuck.net/comments_252082.xml'

xml_url = input('Enter location: ')
print('Retrieving ' + xml_url)

xml = urllib.request.urlopen(xml_url).read()
tree = ET.fromstring(xml)
root = tree.findall('.//comment')

count = 0
sum_number = 0
for child in root:
	number = int(child.find('count').text)
	sum_number += number
	count += 1

print('Count: ' + str(count))
print('Sum: ' + str(sum_number))