import time
from selenium import webdriver

driver = webdriver.Chrome() 
driver.get('http://codepen.io/owlypixel');
time.sleep(3)
search_button = driver.find_element_by_css_selector('.header-search-button')
search_button.click()
# print(elem)
search_box = driver.find_element_by_id('q')
time.sleep(2)
search_box.send_keys('owls')
search_box.submit()
time.sleep(7) 
search_results = driver.find_elements_by_css_selector('.pen-title a')
for pen in search_results:
	if pen.text == 'Owl Generator':
		pen.click()
		break
	# print(pen.text)
	# print(pen.get_attribute('data-slug-hash'))
# driver.quit()