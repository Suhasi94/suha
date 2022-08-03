from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\User\PycharmProjects\APIAutomation\drivers\chromedriver.exe")
url = "https://www.thetestingworldapi.com/"
driver.get(url)