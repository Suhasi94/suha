import requests

url = r"https://reqres.in/api/users/2"

response = requests.delete(url)
print(response)