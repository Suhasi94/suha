import json
import requests
import jsonpath

url = url = r"https://reqres.in/api/users"

file = open(r"C:\Users\User\Desktop\pooja_Api\post_user.json","r")
data = file.read()
json_data = json.loads(data)
#print(json_data)

#make post request with json input body
response = requests.post(url, json_data)
#print(response.content)
#print(response.status_code)

#fetch the headers
#print(response.headers)
#print(response.headers.get('Content-Type'))

#parse response to Json format
response_json = json.loads(response.text)
#pick the id using jsonpath
id = jsonpath.jsonpath(response_json,'id')
print(id[0])


