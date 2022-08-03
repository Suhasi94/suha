import requests
import json
import jsonpath
from selenium import webdriver

url1 = "https://www.thetestingworldapi.com/Help"
driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\APIAutomation\drivers\chromedriver.exe")
url = "https://www.thetestingworldapi.com/Help"
driver.get(url)


#def test_add_student():
    #api_url = "https://thetestingworldapi.com/api/studentsDetails"
    #file_obj = open(r"C:\Users\User\Desktop\pooja_Api\requestjson.json",'r')
    #json_input = file_obj.read()
    #request_json = json.loads(json_input)

    #response = requests.post(api_url, request_json)
    #print(response.content)
