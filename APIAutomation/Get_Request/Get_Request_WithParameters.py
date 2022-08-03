import requests

param = {'name':'pooja','mail':'pooja@gmail.com','number':'+91-9964-038217'}
response = requests.get(r"https://httpbin.org/get",params=param)
print(response.text)
