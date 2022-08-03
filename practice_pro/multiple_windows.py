from selenium import webdriver
from time import sleep

from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
'''

url = "http://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

path = '//a[text()="Twitter"]'
driver.find_element_by_xpath(path).click()

handles = driver.window_handles

driver.switch_to.window(handles[1])
sleep(2)
path1 = '//input[@placeholder="Search Twitter"]'
driver.find_element_by_xpath(path1).send_keys('hello')

sleep(3)

driver.switch_to.window(handles[0])
sleep(2)

driver.find_element_by_xpath('//a[text()="Register"]').click()


################ monster ############
url = 'https://www.monsterindia.com/'
driver.get(url)
driver.maximize_window()
sleep(3)

path = '//input[@placeholder="Search by Skills, Company & Job Title"]'
driver.find_element_by_xpath(path).send_keys('python')

'''

###########3 file download #################3
# it can be done by using ChromeOptions or FireFoxProfile

opts = webdriver.ChromeOptions()
opts.add_experimental_option("prefs",{"download.default_directory":r'C:\Users\User\Desktop\selenium',
                                      "safebrowsing.enabled":True})

#driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe", options=opts)
#driver.get("https://www.whatsapp.com/download/")
#sleep(5)

#driver.find_element_by_xpath("//a[text()='DOWNLOAD FOR WINDOWS']").click()

######### authentication pop up
#url = 'https://the-internet.herokuapp.com/basic_auth'
#driver.get(url)
#driver.maximize_window()

#driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#driver.maximize_window()

################Model window or hidden division pop up ##########
################ calendar popup ###############

url = 'https://www.goibibo.com/'
driver.get(url)
driver.maximize_window()
path = '//span[text()="Departure"]'
driver.find_element_by_xpath(path).click()
sleep(2)
mon = "December 2022"
_day = 1

#selecting the month(assuming that we can book a ticket only 12 months in advance)
for i in range(1,13):
    try:
        driver.find_element_by_xpath(f'//div[text()="{mon}"]')
        break

    except NoSuchElementException:
        driver.find_element_by_xpath('//span[@aria-label="Next Month"]').click()
        continue

try:
    driver.find_element_by_xpath(f'//p[text()="{_day}"]').click()

except NoSuchElementException:
    print('Invalid Date for the given month')


