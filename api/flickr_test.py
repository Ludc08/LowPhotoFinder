import flickrapi

api_key = u'87276a62d22f7ff7ed01e971436a685f'
api_secret = u'3c0a5c7e7645b84d'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
photos = flickr.photos.search(user_id='73509078@N00', per_page='10')
sets = flickr.photosets.getList(user_id='73509078@N00')

print(photos)
