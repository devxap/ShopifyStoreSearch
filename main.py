import requests

with open('API_KEY') as f:
    API_KEY = f.read().strip()

with open('SEARCH_ENGINE_ID') as f:
    SEARCH_ENGINE_ID = f.read().strip()

search_query = 'site:myshopify.com + [Fitness]'

url = 'https://www.googleapis.com/customsearch/v1'

params = {
    'q': search_query,
    'key': API_KEY,
    'cx': SEARCH_ENGINE_ID
}

response = requests.get(url, params=params)

results = response.json()

if 'items' in results:
    for item in results['items']:
        print(item['link'])
