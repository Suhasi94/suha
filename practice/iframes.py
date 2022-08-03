from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")

###################### moving to one frame ####################
'''
url = r"file:///C:/Users/User/Desktop/selenium/html_files/iframe.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

frame1 = driver.find_element_by_xpath('//iframe[@id="FR1"]')
driver.switch_to.frame(frame1)
driver.find_element_by_xpath('//input[@id="small-searchterms"]').send_keys("mobile")
'''


#moving from one frame to another frame
'''
url = r"file:///C:/Users/User/Desktop/selenium/html_files/iframe.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

frame1 = driver.find_element_by_xpath('//iframe[@id="FR1"]')
driver.switch_to.frame(frame1)
driver.find_element_by_xpath('//input[@id="small-searchterms"]').send_keys("mobile")

#moving from one frame to another frame
driver.switch_to.default_content()

frame2 = driver.find_element_by_xpath("//iframe[@id='FR2']")
driver.switch_to.frame(frame2)
driver.find_element_by_xpath('//input[@id="search_form"]').send_keys('Automobiles')
'''

#write a script to find the total number of frames in the web page
url = r"file:///C:/Users/User/Desktop/selenium/html_files/iframe.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

frame1 = driver.find_elements_by_xpath('//iframe')
print("Total number of frames in an web page",len(frame1))