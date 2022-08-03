from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")
driver.implicitly_wait(30)
'''
url = "https://www.myntra.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

#create the instance of actionchains
action = ActionChains(driver)
'''
'''
#######################move to element############################
#move to element:moves the mouse to the middle of an element
#MoveToElement(To Element)
element = driver.find_element_by_xpath('//span[text()="Profile"]')
action.move_to_element(element)
action.perform()

#driver.close()

url = "https://www.monsterindia.com/"
driver.get(url)
driver.maximize_window()
element = driver.find_element_by_xpath('//a[text()="Job search"]')
action = ActionChains(driver)
action.move_to_element(element).perform()

element1 = driver.find_element_by_xpath('//a[text()="Jobs by Skills"]')
action.move_to_element(element1).perform()

element2 = driver.find_element_by_xpath('//a[contains(text(),"Python Jobs")]')
action.move_to_element(element2).perform()
element2.click()
'''
##############################move by offset##################################
#syntax: move_by_offset(xoffset, yoffset)

#element = driver.find_element_by_xpath()
'''
############################double click######################################
url = r"file:///C:/Users/User/Desktop/selenium/html_files/demo.html"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
element = driver.find_elements_by_xpath("//button[text()='Double-click- me']")
#action.double_click(element).perform()
'''

##########################drag and drop###############################
'''
url = r"https://crossbrowsertesting.github.io/drag-and-drop.html"
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)
source_element = driver.find_element_by_xpath('//div[@id="draggable"]')
target_element = driver.find_element_by_xpath('//div[@id="droppable"]')
action.drag_and_drop(source_element, target_element).perform()
'''

############################## send keys ####################################

#url = "http://demowebshop.tricentis.com/"
#driver.get(url)
#driver.maximize_window()

#action = ActionChains(driver)
#action.send_keys(Keys.TAB).perform()
#action.send_keys(Keys.ENTER).perform()
#action.send_keys(Keys.PAGE_DOWN).perform()
#action.send_keys(Keys.PAGE_UP).perform()
#action.send_keys(Keys.ARROW_DOWN).perform()
#action.send_keys(Keys.ARROW_UP).perform()
#action.send_keys(Keys.ESCAPE).perform()


################################ context_click ############################
'''
#-Performs the right click at the current mouse location

url = "http://demowebshop.tricentis.com/"
driver.get(url)
action = ActionChains(driver)
element = driver.find_element_by_xpath("//a[text()='Register']")
#action.context_click(element).perform()#it will right click on the register element
'''