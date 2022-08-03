import jsonpath
import requests
import json


url = r"https://reqres.in/api/users?page=2"

response = requests.get(url)

#get the response as a result <response {200}>
#print(response)

#It is used to get the content present in the url which is in the form of json format
#print(response.content)

#It is used to get headers as well as body
#print(response.headers)

#It is used to validate the status code
#print(response.status_code)
#assert response.status_code == 200

#print(response.headers)

#to get specific content from headers
#print(response.headers.get('Date'))
#print(response.headers.get('server'))

#to get the cookies
#print(response.cookies)

#to get the encoding information
#print(response.encoding)

#to get duration of request and response
#print(response.elapsed)


##### fetch the response content using json path
#first we have to parse the data into json format by using json module
#next by using jsonpath module fetch the specific content present inside the
#content

json_response = json.loads(response.text)
#print(json_response)

#Fetch the value using json path
pages = jsonpath.jsonpath(json_response,"total_pages")
#print(pages[0])

#fetch the first name in data
#first_name = jsonpath.jsonpath(json_response,"data[0]['first_name']")
#print(first_name)


#first_name = jsonpath.jsonpath(json_response,"data[0]")
#print(len(first_name[0]))

for i in range(0,5):
    first_name = jsonpath.jsonpath(json_response,"data["+str(i)+"].first_name")
    print(first_name[0])











