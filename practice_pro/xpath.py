import time

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")

'''
url = r'https://www.myntra.com/kids?f=Categories%3ATshirts%3A%3AGender%3Aboys%2Cboys%20girls&plaEnabled=false'
url1 = "https://www.google.com"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

path = '//input[@placeholder="Search for products, brands and more"]'
element = driver.find_element_by_xpath(path)

'''

############### Locating the Multiple Elements #######################

### check all the checkboxes #####
'''
url = 'file:///C:/Users/User/Desktop/selenium/html_files/demo.html'
driver.get(url)
driver.maximize_window()

ele = driver.find_elements_by_xpath('//input[@name="download"]')

for var in ele:
    var.click()
    time.sleep(3)

### check all the checkboxex in reversed order

for var in ele[::-1]:
    var.click()
    time.sleep(3)

### check alternate checkboxes
for var in ele[::2]:
    var.click()
    time.sleep(3)

### check first and last check Box

ele[0].click()
ele[-1].click()


######### Entering text in all the text boxes in demo web page ##########

path = '//input[@name="fname"]'
ele = driver.find_elements_by_xpath(path)
langauage = ['hello','world','welcome','to','python','selenium','online','tutorial','session']
for i,j in zip(ele,langauage):
    i.send_keys(j)
    time.sleep(3)

### print link text of all the links

url = 'https://www.python.org/'
driver.get(url)
driver.maximize_window()

links = driver.find_elements_by_xpath("//a")
all_links = []
for link in links:
    if link.text != '':
        all_links.append(link.text.strip())

print(all_links)

python_links = []
#list of link text of all the links if the text contains 'python' word init
for link in links:
    if 'python' in link.text or 'Python' in link.text:
        python_links.append(link.text)

print(python_links)

links = driver.find_elements_by_xpath("//a")

urls = []
for link in links:
    if 'python' in link.text or 'Python' in link.text:
        value_href = link.get_attribute("href")
        urls.append((value_href,link.text))

#print(urls)

#print alt tags of all the images present on smart bear webpage

url = r"https://services.smartbear.com/samples/TestComplete14/smartstore/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

images = driver.find_elements_by_xpath("//img")
for image in images:
    print(image.get_attribute("alt"))
    time.sleep(2)

'''
