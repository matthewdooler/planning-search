#!/usr/bin/env python3
import requests
from time import sleep

# 67108 - 2 Dec 2015
startNumber = 69408 # TODO: get this from the highest number (+1) in data directory

i = startNumber
while True:
	filename = str(i) + ".pdf"
	uri = 'https://services.salford.gov.uk/planning/' + filename
	r = requests.get(uri, stream=True)
	if r.status_code == 200:
		with open('data/' + filename, 'wb') as f:
			for block in r.iter_content(1024):
				f.write(block)
		print("Saved " + filename)
	elif r.status_code == 404:
		print("Error " + str(r.status_code) + " for " + filename)
	else:
		print("Error " + str(r.status_code) + " for " + filename)
		r.raise_for_status()
	i = i + 1
	sleep(0.2)

