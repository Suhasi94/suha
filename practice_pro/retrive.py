import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\practice_pro\drivers\chromedriver.exe")
url = "file:///C:/Users/User/Desktop/selenium/html_files/demo.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(30)

'''
path = '//select[@id="standard_cars"]'
element = driver.find_element_by_xpath(path)
select_ = Select(element)
#select by value

select_.select_by_value("aud")
time.sleep(3)
#select by visible text
select_.select_by_visible_text("Honda")
time.sleep(3)
#select by index by default index will start from 1
select_.select_by_index(6)

option = select_.options
#to get text of all the list boxes

for i in option:
    print(i.text)
    time.sleep(3)

#to select all the options in the list boxes
for i in option:
    select_.select_by_visible_text(i.text)
    time.sleep(3)

#select last item of the list boc
#select_.select_by_visible_text(option[-1].text)

#selecting each item in the list box one by one in reverse order
for i in option[::-1]:
    select_.select_by_visible_text(i.text)
    time.sleep(3)
    
#print index at which the "mercedes" is present

for i,j in enumerate(option):
    if j.text == "Mercedes":
        print(f'the index number of "{j.text}" is "{i}"')

## first_selected_option it wii return the option which is currently 
## selected in the list box

select_.select_by_value("aud")
time.sleep(3)
#select by visible text
select_.select_by_visible_text("Honda")
time.sleep(3)
#select by index by default index will start from 1
select_.select_by_index(6)

currently_selected_option = select_.first_selected_option.text
print(currently_selected_option)#last landover



#select_.deselect_by_index(3)
time.sleep(3)

select_.deselect_by_visible_text("Toyota")

select_.select_by_visible_text("Mercedes")
select_.select_by_visible_text("Audi")
select_.select_by_visible_text("Toyota")
all_ = select_.all_selected_options
for item in all_:
    print(item.text)

'''

path = '//select[@id="multiple_cars"]'
list_box = driver.find_element_by_xpath(path)
select = Select(list_box)

select.select_by_visible_text("Audi")
time.sleep(3)
select.select_by_index(3)
time.sleep(3)
select.select_by_value("lr")

ele = select.all_selected_options
for i in ele:
    print(i.text)

#select.deselect_by_visible_text("Audi")
print(select.is_multiple)

print(select.first_selected_option.text)

select.deselect_all()