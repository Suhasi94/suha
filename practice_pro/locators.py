import time

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")

#url = "http://demowebshop.tricentis.com/"
#url1 = "file:///C:/Users/User/Desktop/selenium/html_files/demo.html"
#driver.get(url)
#driver.maximize_window()
#driver.implicitly_wait(50)

#driver.find_element_by_class_name(r"search-box-text.ui-autocomplete-input").send_keys('python')

#print(driver.find_element_by_id("small-searchterms"))

#driver.find_element_by_tag_name("input").send_keys("python")

#driver.find_element_by_name("q").send_keys("mobile")

#driver.find_element_by_link_text("Register").click()

#driver.find_element_by_partial_link_text("Regi").click()

#driver.find_element_by_css_selector('input[value="Search store"]').send_keys('python')

#driver.find_element_by_css_selector('input#small-searchterms').send_keys('python')

#driver.find_element_by_css_selector('input.search-box-text.ui-autocomplete-input').send_keys('python')

#driver.find_element_by_css_selector('input[autocomplete="off"]').send_keys('python')

############# find element by xpath ####################

#absolute Xpath
#relative Xpath

#traversing the absolute path
#absolute xpath can be done with single forward slash(/)

#relative Xpath
#driver.find_element_by_xpath('//a[@class="ico-register"]').click()

#driver.find_element_by_xpath("//a[text()='Register']").click()

#driver.find_element_by_xpath('(//a[contains(@class,"ico-")])[1]').click()
'''
driver.find_element_by_xpath('//td[text()="Ruby"]/..//input[@name="download"]').click()
driver.find_element_by_xpath('//td[text()="Java"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="Perl"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="Python"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="C#"]/..//input[@type="checkbox"]').click()
driver.find_element_by_xpath('//td[text()="JavaScript"]/..//input[@type="checkbox"]').click()

languages = ["Ruby", "Java", "Perl", "Python", "C#", "JavaScript"]

for i in languages:
    path = f'//td[text()="{i}"]/..//input[@type="checkbox"]'
    driver.find_element_by_xpath(path).click()
    time.sleep(3)
'''
#path = '//a[text()="Computing and Internet"]/../..//input[@value="Add to cart"]'

'''
url = "http://demowebshop.tricentis.com/books"
driver.get(url)
driver.maximize_window()

#driver.find_element_by_xpath(path).click()
#driver.find_element_by_xpath('//a[text()="Fiction"]/../..//input[@value="Add to cart"]').click()
#driver.find_element_by_xpath('//a[text()="Health Book"]/../..//input[@value="Add to cart"]').click()

books = ["Computing and Internet", "Fiction", "Health Book"]

for i in books:
    path = f'//a[text()="{i}"]/../..//input[@value="Add to cart"]'
    driver.find_element_by_xpath(path).click()
    time.sleep(3)

url = "http://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()

ratings = ["Excellent", "Good", "Poor", "Very bad"]
for rate in ratings:
    path = f'//strong[text()="Do you like nopCommerce?"]/..//label[text()="{rate}"]'
    driver.find_element_by_xpath(path).click()
    time.sleep(3)

##########validate the actual prices of all the books
 against the expected price##########################

url = "http://demowebshop.tricentis.com/books"
driver.get(url)
driver.maximize_window()

expected_price = {"Science": 100.00, "Health Book": 10.00, 'Fiction': 24.00, "Computing and Internet": 10.00}

for book,price in expected_price.items():
    path = f'//a[text()="{book}"]/../..//span[@class="price actual-price"]'
    actual_price = driver.find_element_by_xpath(path).text

    if float(actual_price) == price:
        print("PASS")

    else:
        print("FAIL")
        print(f"the actual price of {book} book is {actual_price} and the expected price is {price}")

'''

############# get the price tag of all the sun glasses ############
'''
url = "https://services.smartbear.com/samples/TestComplete14/smartstore/sunglasses"
driver.get(url)
driver.maximize_window()

glass_names = ["Sunglasses Aero", "ORIGINAL COLLECTION", "Custom Sunglasses"]

expected_price = {"Sunglasses Aero": 139.00, "ORIGINAL COLLECTION": 149.00, "Custom Sunglasses": 179.00}


for price in glass_names:
    path = f'//span[text()="{price}"]/../../..//span[@class="art-price"]'
    tag_price = driver.find_element_by_xpath(path).text
    print(tag_price)

import re

#validate actual with the expected price
for glass, price in expected_price.items():
    path = f'//span[text()="{glass}"]/../../..//span[@class="art-price"]'
    actual_price = driver.find_element_by_xpath(path).text
    print(actual_price)
    tag_price = re.findall(r'\d+.\d+',actual_price)
    tag_price = float(tag_price[0])

    if tag_price == price:
        print("Pass")

    else:
        print("Fail")

'''

############ get the share price dynamically ##################
'''
url = 'https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market'
driver.get(url)
driver.maximize_window()

companies = ['TCS', 'WIPRO', 'BAJAJFINSV']

for i in companies:
    path = f"//a[text()='{i}']/../..//td[7]"
    share = driver.find_element_by_xpath(path).text
    print(share)


for company in companies:
    print(f"{company:>15}", end='')

#print()
#print('-'*55)

for company in companies:
    path = f"//a[text()='{company}']/../..//td[7]"
    share = driver.find_element_by_xpath(path).text
    print(f"{share:>15}",end='')
    
'''

#### get the link of all the links present in left navigation bar in
## demowebshop website ###

#url = "http://demowebshop.tricentis.com/"
#driver.get(url)
#driver.maximize_window()

'''
path = '//div[@class="block block-category-navigation"]//a'
links = driver.find_elements_by_xpath(path)

for link in links:
    print(link.text)


path = '//div[@class="footer-menu-wrapper"]//a'
footer_links = driver.find_elements_by_xpath(path)
for i in footer_links:
    print(i.text)

'''

'''
### get link text of all footer links in smart bear webpage########
url = 'https://services.smartbear.com/samples/TestComplete14/smartstore/'
driver.get(url)
driver.maximize_window()

path = '//div[@class="footer-main-wrapper"]//a'
footer_link = driver.find_elements_by_xpath(path)
for link in footer_link:
    print(link.text)

'''
################# doubt########################
#get link text of all job titles in search results of monster.com
'''
url = "https://www.monsterindia.com/"
driver.get(url)
driver.maximize_window()

driver.find_element_by_xpath("//input[@id='SE_home_autocomplete']").send_keys("python")
time.sleep(3)
driver.find_element_by_xpath("//strong[text()='Python']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@value='Search']").click()
time.sleep(3)

path = r'//div[@class="job-tittle"]/h3/a'
job_tittles = driver.find_elements_by_xpath(path)
for i in job_tittles:
    print(i.text)

'''
##doubt
#get the actual price tag of all the new products in smart bear webpage#
'''
url = 'https://services.smartbear.com/samples/TestComplete14/smartstore/newproducts'
driver.get(url)
driver.maximize_window()


path1 = '//div[@id="artlist-1905121599"]//article[@class="art"]//h3/a'
ele = driver.find_elements_by_xpath(path1)
print(ele)


for i in ele:
    path = '//span[text()="Podium Big Size"]/../../..//span[@class="art-price"]'
    price = driver.find_elements_by_xpath(path).text
    print(price)
'''

## extracting tshirt name and discount of all
# discounted tshirts in myntra.com

url = r'https://www.myntra.com/kids?f=Categories%3ATshirts%3A%3AGender%3Aboys%2Cboys%20girls&plaEnabled=false'
driver.get(url)
driver.maximize_window()
'''
path = '//span[@class="product-discountPercentage"]'
element_discount = driver.find_elements_by_xpath(path)

path1 = '//span[@class="product-discountPercentage"]/../..//h4[@class="product-product"]'
element_tshirts = driver.find_elements_by_xpath(path1)

#print(element_discount)
#print("--------------------------------------------------")
#print(element_tshirts)

discount = [i.text for i in element_discount]

shirts = [i.text for i in element_tshirts]

actual_discount = []
for i,j in zip(shirts, discount):
    actual_discount.append((i,j))

print(len(actual_discount))
'''
### filtering only "PEPE JEANS" T-shirts


path = '//input[@placeholder="Search for products, brands and more"]'
element = driver.find_element_by_xpath(path).send_keys("PEPE JEANS")
time.sleep(3)
element.click()

