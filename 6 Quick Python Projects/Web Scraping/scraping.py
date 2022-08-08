# Scraping the Profile image

 # https://docs.python-requests.org/en/latest/
import requests
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup as bs 

# Custom exception
class UsernameNotFoundError(Exception):
	pass

def fetch_profile_image(username):
	url = f'https://github.com/{username}'
	req = requests.get(url)

	if req.status_code == 200:
		# user's html content
		soup = bs(req.content, 'html.parser')
		profile_image = soup.find('img', {'alt': 'Avatar'})['src']
		return profile_image
	else:
		raise UsernameNotFoundError(f'https:github.com/{username} not found')

username = input('Github Username: ')
print(fetch_profile_image(username))