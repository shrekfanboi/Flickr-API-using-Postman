# Flickr-API-using-Postman
A demo of using the Flickr API through Postman
FLICKR API
The api documentation is provided at https://www.flickr.com/services/api/
We obtain the API key and the secret Key
We go to https://www.flickr.com/services/api/flickr.photos.getPopular.htm
API Specifications:
Authentication
This method does not require authentication.

Arguments
api_key (Required)
Your API application key. See here for more details.
user_id (Optional)
The NSID of the user to get a galleries list for. If none is specified, the calling user is assumed.
sort (Optional)
The sort order. One of faves, views, comments or interesting. Defaults to interesting.
extras (Optional)
A comma-delimited list of extra information to fetch for each returned record. Currently supported fields are: description, license, date_upload, date_taken, owner_name, icon_server, original_format, last_update, geo, tags, machine_tags, o_dims, views, media, path_alias, url_sq, url_t, url_s, url_q, url_m, url_n, url_z, url_c, url_l, url_o
per_page (Optional)
Number of photos to return per page. If this argument is omitted, it defaults to 100. The maximum allowed value is 500.
page (Optional)
The page of results to return. If this argument is omitted, it defaults to 1.


We test the API in https://www.flickr.com/services/api/explore/flickr.photos.getPopular
We provide the api key and the user-id.
The output format is selected as JSON
Selecting Do not sign call
We call the method and can already check the output
We copy the url and go to https://www.postman.com/
We paste the url  
https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=3890e3bef54cafedd35829b049bc5d70&user_id=193817164%40N07&format=json&nojsoncallback=1
We make a GET request and check the status code for validation.

