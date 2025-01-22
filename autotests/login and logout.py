#тестирование процесса входа в аккаунт

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text('My Account')
my_account.click()

reg_email = driver.find_element_by_id('reg_email')
reg_email.send_keys('zverevatoria@yandex.ru')

reg_password = driver.find_element_by_id('reg_password')
reg_password.send_keys('22028875Vk')

register = driver.find_element_by_css_selector('[name="register"]')
register.click()
 driver.quit()



#тестирование процесса выхода из аккаунта


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

my_account = driver.find_element_by_link_text('My Account')
my_account.click()

login = driver.find_element_by_id('username')
login.send_keys('zverevatoria@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('22028875Vk')

login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()

logout = driver.find_elements_by_link_text('Logout')
if logout:
    print("Элемент есть на сайте")
else:
    print("Элемента нет на сайте")
 driver.quit()