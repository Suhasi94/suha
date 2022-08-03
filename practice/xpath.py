import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")
'''
url = "file:///C:/Users/User/Desktop/selenium/html_files/demo.html"

driver.get(url)

driver.maximize_window()

#xpath by attribute
element = driver.find_element_by_xpath("//a[@class='ico-register']")
print(element)
element.click()

#xpath by text function
element = driver.find_element_by_xpath("//a[text()='Register']")
element.click()

#xpath by using contains
#//input[contains(@class,"textField")] by using attribute
#//input[conatins(text(),"Books")] by using text
#//a[contains(@class,"ico-")]

#xpath by using indexing(group indexing)
#(//a[contains(text(),"Books")])[1]

#to check all the check boxes
driver.find_element_by_xpath('//td[text()="Ruby"]/..//input[@name="download"]').click()
driver.find_element_by_xpath('//td[text()="Java"]/..//input[@name="download"]').click()
driver.find_element_by_xpath('//td[text()="Perl"]/..//input[@name="download"]').click()
driver.find_element_by_xpath('//td[text()="Python"]/..//input[@name="download"]').click()
driver.find_element_by_xpath('//td[text()="C#"]/..//input[@name="download"]').click()
driver.find_element_by_xpath('//td[text()="JavaScript"]/..//input[@name="download"]').click()


#find element(loc_name,loc_value)

languages = ["Ruby", "Java", "Perl", "Python", "C#", "JavaScript"]
#check the checkboxes in forward direction.
for language in languages:
    x_path = f'//td[text()="{language}"]/..//input[@name="download"]' #dynamic path
    #driver.find_element_by_xpath(x_path).click()
    #time.sleep(2)

#check the checkboxes in reverse direction
for language in languages[::-1]:
    x_path = f'//td[text()="{language}"]/..//input[@name="download"]' #dynamic path
    driver.find_element_by_xpath(x_path).click()
    time.sleep(2)


url = "http://demowebshop.tricentis.com/"

driver.get(url)
driver.maximize_window()

elements = driver.find_elements_by_xpath('//div[@class="block block-category-navigation"]//a')
#print(elements)

for ele in elements:
    print(ele.text)

#//div[@class="footer-menu-wrapper"]//a footer elements to match

url = "file:///C:/Users/User/Desktop/selenium/html_files/parent_child.html"
driver.get(url)
driver.maximize_window()

menu = '//input[@type="checkbox"]'
menu1 = '//a'
elements = driver.find_elements_by_xpath(menu1)
print(len(elements))
'''


url = "file:///C:/Users/User/Desktop/selenium/html_files/demo.html"
driver.get(url)
driver.maximize_window()

menu = "//input[@type='checkbox']"
menu1 = '//input[@name="download"]'

elements = driver.find_elements_by_xpath(menu1)

for ele in elements:
    ele.click()
    time.sleep(1)
