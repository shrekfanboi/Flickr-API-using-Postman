import requests
payload = {
    "method":"flickr.photos.getPopular",
    "api_key":"3890e3bef54cafedd35829b049bc5d70",
    "user_id":"193817164@N07",
    "format":"json",
    "nojsoncallback":"1"
}
r = requests.get("https://www.flickr.com/services/rest/",params=payload)
if(r.status_code == 200):
    print(r.json())
else:
    print("Call was unsuccessful")
