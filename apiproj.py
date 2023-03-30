import requests

url = 'https://api.dictionaryapi.dev/api/v2/entries/en/yauoza'

response = requests.get(url)

print(response)