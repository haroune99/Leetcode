import requests, json

url = 'https://www.sofascore.com/api/v1/event/13302065/lineups'

response = requests.request('GET',url)
jsondata = json.loads(response.text)
print(jsondata)


