import urllib.request
import json

# sample_url = 'http://python-data.dr-chuck.net/comments_42.json'
# actual_url = 'http://python-data.dr-chuck.net/comments_252086.json'

json_url = input('Enter location: ')
print('Retrieving: ' + json_url)

response = urllib.request.urlopen(json_url).read()
response = response.decode("utf-8")
result = json.loads(response)

comment_count = 0
comment_sum = 0
for comment in result['comments']:
	comment_count += 1
	comment_sum += int(comment['count'])

print('Count: ' + str(comment_count))
print('Sum: ' + str(comment_sum))