from urllib.parse import urlencode
import urllib.request
import json

# test_address = 'South Federal University'
# actual_address = 'International Institute of Information Technology Hyderabad'
address = input('Enter location: ')
request_data = {
	'sensor': False,
	'address': address
}

service_url = 'http://python-data.dr-chuck.net/geojson?'
request_url = service_url + urlencode(request_data)
print('Retrieving: ' + request_url)

response = urllib.request.urlopen(request_url).read()
response = response.decode("utf-8")
results = json.loads(response)
print('Place id ' + results['results'][0]['place_id'])