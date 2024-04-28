import requests
URL = 'https://httpbin.org/'
response = requests.get(URL + 'image', headers={"accept": "image/png"})
print(response)
