#1

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

Shop = driver.find_element_by_link_text('Shop')
Shop.click()

Html5 = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
Html5.click()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

title = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[itemprop='name']"), "HTML5 Forms"))
 driver.quit()

#2

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

Shop = driver.find_element_by_link_text('Shop')
Shop.click()

HTML = driver.find_element_by_link_text('HTML')
HTML.click()

items_count = driver.find_elements_by_class_name('woocommerce-LoopProduct-link')
if len(items_count) == 3:
    print('На странице 3 товара')
else:
    print('Количество товаров на странице:' + str(len(items_count)))
 driver.quit()


#3

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
from selenium.webdriver.support.select import Select

my_account = driver.find_element_by_link_text('My Account')
my_account.click()

login = driver.find_element_by_id('username')
login.send_keys('zverevatoria@gmail.com')

password = driver.find_element_by_id('password')
password.send_keys('22028875Vk')

login_btn = driver.find_element_by_css_selector('[name="login"]')
login_btn.click()

Shop = driver.find_element_by_link_text('Shop')
Shop.click()

selector = driver.find_element_by_name('orderby')

default = selector.find_element_by_css_selector('[value="menu_order"]')
default_checked = default.get_attribute('selected')
if default_checked is not None:
    print("В селекторе выбран вариант сортировки по умолчанию")
else:
    print("В селекторе НЕ выбран вариант сортировки по умолчанию")

select = Select(selector)
select.select_by_value('price-desc')

selector = driver.find_element_by_name('orderby')

price_desc = driver.find_element_by_css_selector('[value="price-desc"]')
price_desc_checked =price_desc.get_attribute('selected')
if price_desc_checked is not None:
    print("В селекторе выбран вариант сортировки по цене от большей к меньшей")
else:
    print("В селекторе НЕ выбран вариант сортировки по цене от большей к меньшей")

 driver.quit()


#4
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

Shop = driver.find_element_by_link_text('Shop')
Shop.click()

Android = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
Android.click()

Price_1 = driver.find_element_by_css_selector('del .woocommerce-Price-amount')
Price_1_get_text = Price_1.text
assert Price_1_get_text == '₹600.00'

Price_2 = driver.find_element_by_css_selector('ins .woocommerce-Price-amount')
Price_2_get_text = Price_2.text
assert Price_2_get_text == '₹450.00'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
cover = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']")))
cover.click()

wait = WebDriverWait(driver, 10)
cross = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
cross.click()
 driver.quit()



#5
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("https://practice.automationtesting.in/")

Shop = driver.find_element_by_link_text('Shop')
Shop.click()

backet = driver.find_element_by_css_selector('[data-product_id="182"]')
backet.click()

time.sleep(5)

items = driver.find_element_by_class_name('cartcontents')
items_get_text = items.text
assert items_get_text == '1 Item'

cost = driver.find_element_by_css_selector('.wpmenucart-contents .amount')
cost_get_text = cost.text
assert cost_get_text == '₹180.00'

backet_btn = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
backet_btn.click()

Subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "₹180.00"))

total = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount"), "₹183.60"))
 driver.quit()

#6


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
driver.get("https://practice.automationtesting.in/")

Shop = driver.find_element_by_link_text('Shop')
Shop.click()

driver.execute_script("window.scrollBy(0, 300);")

HTML_book = driver.find_element_by_css_selector('[data-product_id="182"]')
HTML_book.click()

time.sleep(10)

JS = driver.find_element_by_css_selector('[data-product_id="180"]')
JS.click()

time.sleep(5)

backet_btn = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
backet_btn.click()

time.sleep(5)

cross = driver.find_element_by_css_selector('[data-product_id="182"]')
cross.click()

time.sleep(5)

undo = driver.find_element_by_link_text('Undo?')
undo.click()

time.sleep(10)

quantity = driver.find_element(By.NAME, "cart[045117b0e0a11a242b9765e79cbf113f][qty]")
quantity.clear()
time.sleep(5)
quantity.send_keys('3')

time.sleep(5)

update_cart = driver.find_element_by_css_selector('[name="update_cart"]')
update_cart.click()

time.sleep(5)

quantity = driver.find_element(By.NAME, "cart[045117b0e0a11a242b9765e79cbf113f][qty]")
quantity_value = quantity.get_attribute('value')
print(quantity_value)
assert quantity_value == '3'

time.sleep(10)

apply_coupon = driver.find_element_by_css_selector('[name="apply_coupon"]')
apply_coupon.click()

text = driver.find_element_by_css_selector('.woocommerce-error li')
text_get_text = text.text
assert text_get_text == 'Please enter a coupon code.'
 driver.quit()

#7

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
driver.get("https://practice.automationtesting.in/")

Shop = driver.find_element_by_link_text('Shop')
Shop.click()

driver.execute_script("window.scrollBy(0, 300);")

HTML_book = driver.find_element_by_css_selector('[data-product_id="182"]')
HTML_book.click()

time.sleep(10)

backet_btn = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
backet_btn.click()

time.sleep(10)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

checkout_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button.button.alt.wc-forward')))
checkout_button.click()

first_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'billing_first_name')))
first_name.send_keys('Vika')

last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Zvereva')

email = driver.find_element_by_id('billing_email')
email.send_keys('zverevatoria@gmail.com')

phone = driver.find_element_by_id('billing_phone')
phone.send_keys('89992202882')

country = driver.find_element_by_id('s2id_billing_country')
country.click()
search = driver.find_element_by_id('s2id_autogen1_search')
search.send_keys('Angola')
angora = driver.find_element_by_id('select2-results-1')
angora.click()

adress = driver.find_element_by_id('billing_address_1')
adress.send_keys('alalala')

billing_state = driver.find_element_by_id('billing_state')
billing_state.send_keys('lalala')

postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('1234')

town = driver.find_element_by_id('billing_city')
town.send_keys('dhdfth')

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(10)

option = driver.find_element_by_css_selector('[value="cheque"]')
option.click()

place_order = driver.find_element_by_id('place_order')
place_order.click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Thanks = WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

check_payment = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))

 driver.quit()