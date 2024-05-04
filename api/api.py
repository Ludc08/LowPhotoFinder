import requests
URL = 'https://httpbin.org/'
#param = 'Следующее утверждение верно. Предыдущее утверждение ложно'
response = requests.get(f'{URL}/status/418')
#response = requests.get(URL + 'image', headers={"accept": "image/png"})
#with open('image.png', 'wb') as f:
#    f.write(response.content)
print(response.text)
