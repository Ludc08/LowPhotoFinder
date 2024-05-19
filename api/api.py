import xml.etree.ElementTree as ET
import requests
URL = 'https://www.flickr.com/services/rest/'
key = u'87276a62d22f7ff7ed01e971436a685f'
Secret = '3c0a5c7e7645b84d'
method_query = '?method='
method = 'flickr.photos.getRecent' 
params = {'api_key': key}
response = requests.get(URL + method_query + method, params=params)

tree = ET.ElementTree(ET.fromstring(response.content))
count = 0
root = tree.getroot()
for child in root.iter('photo'):
    url=f'https://live.staticflickr.com/{child.attrib['server']}/{child.attrib['id']}_{child.attrib['secret']}_b.jpg'
    response = requests.get(url, stream = True)
    with open(f'pict{count}.jpg', 'wb') as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
    count += 1
