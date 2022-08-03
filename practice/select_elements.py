import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice\drivers\chromedriver.exe")

url = "file:///C:/Users/User/Desktop/selenium/html_files/demo.html"

driver.get(url)
driver.maximize_window()
'''
element = driver.find_element_by_xpath('//select[@id="standard_cars"]')

select_obj = Select(element)

select_obj.select_by_index(2)
time.sleep(1)
select_obj.select_by_value("hda")
time.sleep(1)
select_obj.select_by_visible_text("Jaguar")
'''
#l1 = select_obj.all_selected_options

#to select all the options present in the select car
#l2 = select_obj.options
#print(l2)
#for option in l2:
    #print(option.text)

#to select the first element in the web page
#l3 = select_obj.first_selected_option
#print(l3.text)

#select all the elements one by one
#option = select_obj.options
#using text
#for ele in option:
    #select_obj.select_by_visible_text(ele.text)
    #time.sleep(1)
'''

#using index
all_options = select_obj.options
#1)range function
for index in range(len(all_options)):
    select_obj.select_by_index(index)
    time.sleep(1)

#2)enumerate
for index,element in enumerate(all_options):
    select_obj.select_by_index(index)
    time.sleep(1)
'''

####################### multi-select list boxes ########################

element = driver.find_element_by_xpath('//select[@id="multiple_cars"]')

s_obj = Select(element)


s_obj.select_by_index(1)
time.sleep(1)
s_obj.select_by_value("bmw")
time.sleep(1)
s_obj.select_by_value("sel")

time.sleep(1)
all_options = s_obj.options
'''
for i in all_options:
    s_obj.select_by_visible_text(i.text)
    time.sleep(1)

time.sleep(3)
#to get only selected options
selected_options = s_obj.all_selected_options
for i in selected_options:
    print(i.text)
    s_obj.select_by_visible_text(i.text)
    time.sleep(1)

first_sel_opt = s_obj.first_selected_option
print(first_sel_opt.text)
'''

s_obj.deselect_all()

#facebook register page -->date of birth --> date, month, year
#open demowebshop -->sort the books and -->add the fiction to the cart