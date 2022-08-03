from selenium import  webdriver

driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\python\driver\chromedriver.exe')

driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()