from selenium import webdriver
import os
import time

try:
	link = 'http://suninjuly.github.io/file_input.html'
	browser = webdriver.Chrome()
	browser.get(link)

	name = browser.find_element_by_name('firstname')
	name.send_keys('Ivan')
	lastname = browser.find_element_by_name('lastname')
	lastname.send_keys('Ivanov')
	email = browser.find_element_by_name('email')
	email.send_keys('test@mail.ru')
	# inport file
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'lesson11.txt')
	import_button = browser.find_element_by_id('file')
	import_button.send_keys(file_path)
	# submit button
	button = browser.find_element_by_css_selector('button')
	button.click()

finally:
	time.sleep(15)
	browser.quit()
