
import requests
while True:
	command = raw_input('command? ').strip() 
	# You want to get a list of places you can hangout in from http://www.hangout.co.ke/concerts/
	
		# trying to get a list of dictionaries that represent a single task 
		# Let us say you want to get a list of action items, via the GET /concerts/ endpoint:
	if command == 'Get':
		response = requests.get('http://www.hangout.co.ke/')
		if response.status_code != 200:
    		# it means that something is not right.
    			raise ApiError('GET/concerts/ {}'.format(response.status_code))
		for concert in response.json():
    			print('{} {}'.format(concert['name'], concert['summary']))
#using POST

	elif command =='POST':

		concert = {"name": "", "description": "" }

		response = requests.post('http://www.hangout.co.ke/', json=place)
		if response.status_code != 201:
    			raise ApiError('POST /concerts/ {}'.format(response.status_code))
		print('Created concert.name: {}'.format(response.json()["id"]))