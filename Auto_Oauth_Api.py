import requests
import json
url="https://www.flickr.com/services/rest?oauth_consumer_key=343be61744a039016ef02a4bee0e3745&oauth_token=72157720815687458-cf9f36c07fe031af&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1632394439&oauth_nonce=6nDLxZ&oauth_version=1.0&oauth_signature=JiNarAwVBDi0PIhOsUQp2gLVoM4=&nojsoncallback=1&format=json&method=flickr.test.login"

try:
	r=requests.get(url)

	data=r.json()

	data=json.dumps(data,indent=1)

	print("OauthAPI Output =>\n\n")
	print(data)

	print("\n\nOauth API Status code =>",r.status_code,"\n")

except:
	print("\nPlease put the URL correctly.")