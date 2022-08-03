import time
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")
'''
url = "file:///C:/Users/User/Desktop/selenium/html_files/demo.html"

driver.get(url)

multi_element = driver.find_elements("name","fname")

languages = ['python', 'java', 'c#', 'sql', 'selenium', 'web', 'c++', 'angular', 'django']


for ele1,ele2 in zip(multi_element,languages):
    ele1.send_keys(ele2)
    time.sleep(1)
    
'''

url = "https://www.python.org/"
driver.get(url)
driver.maximize_window()

elements = driver.find_elements("xpath","//a")
elements1 = driver.find_elements("tag name","a")

output = []
res=[]

for ele in elements:
    print(ele.get_attribute("href"))
    if ele.text=='':
        continue

    else:
        output.append(ele.text)


print(output)


