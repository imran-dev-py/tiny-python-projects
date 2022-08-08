# fetch user's public repos

import requests
from pprint import pprint

def fetch_public_repos(login):
	url = f'https://api.github.com/search/repositories?q=user:{login}'
	req = requests.get(url)
	data = req.json()

	for key in data['items']:
		for k, v in key.items():
			if k == 'full_name': 
				yield v

username = input('Github Username: ')
for repo in fetch_public_repos(username):
	print(repo)