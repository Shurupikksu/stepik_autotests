from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = 'http://suninjuly.github.io/alert_accept.html'
	browser = webdriver.Chrome()
	browser.get(link)

	# Button click
	button = browser.find_element_by_css_selector('button')
	button.click()
	# Alert switch and confirm
	confirm = browser.switch_to.alert
	confirm.accept()
	# Calc on another page
	x_element = browser.find_element_by_id('input_value')
	x = x_element.text
	y = calc(x)
	input_answer = browser.find_element_by_id('answer')
	input_answer.send_keys(y)
	submit_button = browser.find_element_by_css_selector('button.btn')
	submit_button.click()

finally:
	time.sleep(15)
	browser.quit()
