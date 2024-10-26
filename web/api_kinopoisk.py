from requests import get

from itertools import batched
from json import load, dumps
from pathlib import Path
from pprint import pprint
from sys import path


api_url = 'https://api.kinopoisk.dev'

token = Path(...).read_text().strip()

with open(Path(path[0]) / 'kinopoisk_serach_movie_by_word.api_headers') as filein:
    params = load(filein)

search = 'терминатор'
search_enc = ''
for h in batched(search.encode().hex(), n=2):
    search_enc += f'%{"".join(h).upper()}'

params['headers']['X-API-KEY'] = token
params['query'] = search_enc


response = get(
    url=f'{api_url}/v1.4/movie/search?limit=250&query={search_enc}',
    headers=params['headers']
)
results = response.json()['docs']


movie_id = results[0]['id']
response = get(
    url=f'{api_url}/v1.4/person?limit=250&selectFields=&movies.id={movie_id}',
    headers=params['headers']
)
actors = response.json()['docs']

for actor in actors:
    print(actor['name'])

