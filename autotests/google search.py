from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.google.com')

search = find_element_by_class_name('Alh6id')
search.send_keys('test')

empty_space = find_element_by_css_selector('.o3j99 .LLD4me .yr19Zb .LS8OJ')
empty_space.click()

searh_button = find_element_by_class_name('gNO89b')
searh_button.click()

result = find_element_by_id('center_col')
if len(result) < 0:
    print ('Результаты поиска не отображаются')
else len(result) > 0:
    print ('Результаты поиска отображаются. Найдено {len(result)} результатов.')

 driver.quit()