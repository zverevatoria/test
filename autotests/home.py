from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")

Selenium_Ruby = driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 h3')
Selenium_Ruby.click()

Reviews = driver.find_element_by_class_name('reviews_tab')
Reviews.click()

star_5 = driver.find_element_by_class_name('star-5')
star_5.click()

comment = driver.find_element_by_id('comment')
comment.send_keys('Nice book!')

name = driver.find_element_by_id('author')
name.send_keys('Vika')

email = driver.find_element_by_id('email')
email.send_keys('zvereva@yandex.ru')

submit = driver.find_element_by_id('submit')
submit.click()
 driver.quit()