import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")

'''
url = "https://www.myntra.com/"
driver.get(url)
driver.maximize_window()
time.sleep(5)
actions = ActionChains(driver)
profile = driver.find_element_by_xpath('//span[text()="Profile"]')
# Mouse over on "Profile"
actions.move_to_element(profile).perform()
driver.find_element_by_xpath('//a[text()="login / Signup"]').click()
'''
'''
##########monster.com-->job search-->job by skills-->python jobs
url = "https://www.monsterindia.com/"
driver.get(url)
driver.maximize_window()
time.sleep(5)
action = ActionChains(driver)

job_searchs = driver.find_element_by_xpath('//a[text()="Job search"]')

action.move_to_element(job_searchs).perform()
time.sleep(3)

job_skills = driver.find_element_by_xpath('//a[text()="Jobs by Skills"]')

action.move_to_element(job_skills).perform()
time.sleep(3)

python_jobs = driver.find_element_by_xpath('//a[contains(text(),"Python Jobs")]')

action.move_to_element(python_jobs).perform()
time.sleep(3)

python_jobs.click()
'''
'''
############# send_keys #######################
url = 'http://demowebshop.tricentis.com/'
driver.get(url)
driver.maximize_window()
time.sleep(5)

action = ActionChains(driver)
action.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(3)
action.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(3)
action.send_keys(Keys.ARROW_LEFT).perform()
time.sleep(3)
action.send_keys(Keys.PAGE_UP).perform()
'''
'''
######### context_click ###############
url = 'http://demowebshop.tricentis.com/'
driver.get(url)
driver.maximize_window()
time.sleep(5)

register_link = driver.find_element_by_xpath('//a[text()="Register"]')

action = ActionChains(driver)
action.context_click(register_link).perform()
'''

######### drag and drop ################

url = r"https://crossbrowsertesting.github.io/drag-and-drop.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

action = ActionChains(driver)

source_element = driver.find_element_by_xpath('//div[@id="draggable"]')

target_element = driver.find_element_by_xpath('//div[@id="droppable"]')

action.drag_and_drop(source_element, target_element).perform()