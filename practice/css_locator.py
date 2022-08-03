import time
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")

url = "http://demowebshop.tricentis.com/"

driver.get(url)

driver.maximize_window()

'''
#by id
element = driver.find_element_by_id("small-searchterms")
print(element)

#by name
element = driver.find_element_by_name("q")
print(element)

#by class name
element = driver.find_element_by_class_name("search-box-text.ui-autocomplete-input")
print(element)
element.send_keys("mobiles")
############################## css selector ################################
#by using css_selector
element = driver.find_element_by_css_selector("input[value='Search store']")
print(element)
element.send_keys("phone")

#css_selector by using attribute
element = driver.find_element_by_css_selector("input[autocomplete='off']")
print(element)
element.send_keys("phone")

#css_selector by using id
element = driver.find_element_by_css_selector("input#small-searchterms")
print(element)

#css_selector by using class name
element = driver.find_element_by_css_selector("input.search-box-text.ui-autocomplete-input")
print(element)


########################## link text locator #################################
element = driver.find_element_by_link_text("Register")
element.click()
time.sleep(3)

########################## partial link text #################################
driver.back()
time.sleep(3)

link = driver.find_element_by_partial_link_text("Regi")
print(link)
link.click()

############################ xpath #####################################
#xpath by attribute
element = driver.find_element_by_xpath("//a[@class='ico-register']")
print(element)
element.click()

#xpath by text function
element = driver.find_element_by_xpath("//a[text()='Register']")
element.click()
'''
#xpath by using contains
#//input[contains(@class,"textField")] by using attribute
#//input[conatins(text(),"Books")] by using text
#//a[contains(@class,"ico-")]

#xpath by using indexing(group indexing)
#(//a[contains(text(),"Books")])[1]

