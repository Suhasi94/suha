import requests

#add the the data into the headers
headers_data = {'T1': 'First_header' , 'T2': 'Second_header'}

response = requests.get(r"https://httpbin.org/get", headers=headers_data)
print(response.text)