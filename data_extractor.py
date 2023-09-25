import requests
import os
from dotenv import load_dotenv

load_dotenv() 

url = 'https://api.github.com/graphql'
json = {"query": "query {viewer {contributionsCollection {contributionCalendar {totalContributions weeks{ contributionDays{ contributionCount date}}}}}}"}
api_token = os.getenv('API_TOKEN') 
headers = {'Authorization': 'token %s' % api_token}
r = requests.post(url=url, json=json, headers=headers)
print(r.text)
