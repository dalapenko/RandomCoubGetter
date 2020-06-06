import requests
import json

class Coub(object):
	def __init__(self):
		self.siteUrl = 'https://coub.com'
		self.apiUrl = 'http://coub.com/api/v2'
		
	def getRandom(self):
		url = f'{self.apiUrl}/timeline/explore/random'
		response = requests.get(url)
		todos = json.loads(response.text)

		coubs_on_page = todos['coubs']
		random_coub_link = coubs_on_page[1]['permalink']

		coub = f'{self.siteUrl}/view/{random_coub_link}'

		return coub
