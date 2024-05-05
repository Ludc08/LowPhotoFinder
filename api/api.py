import requests
URL = 'https://www.flickr.com/services/rest/'
Key = u'87276a62d22f7ff7ed01e971436a685f'
Secret = '3c0a5c7e7645b84d'
#param = 'Следующее утверждение верно. Предыдущее утверждение ложно'
# response = requests.get(f'{URL}/status/418')
method = '?method=flickr.auth.oauth.getAccessToken'
arguments = '&api_key={Secret}:{Key}'
# response = requests.get(URL + 'image', headers={"accept": "image/svg+xml"})
# with open('image.svg+xml', 'wb') as f:
#     f.write(response.content)

response = requests.get(URL + method + arguments)
print(response)
print(response.headers)
print(response.content)
print(response.json())
