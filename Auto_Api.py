import requests
import json
url="https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=343be61744a039016ef02a4bee0e3745&user_id=193993151%40N07&format=json&nojsoncallback=1"


try:
	r=requests.get(url)

	data=r.json()

	data=json.dumps(data,indent=1)

	print("API Output =>\n\n")
	print(data)

	print("\n\nAPI Status code =>",r.status_code,"\n")

except:
	print("\nPlease put the URL correctly.")