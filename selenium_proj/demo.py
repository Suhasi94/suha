from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\selenium_proj\drivers\chromedriver.exe")

url = r"https://www.google.com/"

driver.get(url)