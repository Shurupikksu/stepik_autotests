from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = 'http://suninjuly.github.io/redirect_accept.html'
	browser = webdriver.Chrome()
	browser.get(link)

	# Button click
	button_troll = browser.find_element_by_css_selector('button.trollface')
	button_troll.click()
	# Switch window
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	# Catch X and calc
	x_element = browser.find_element_by_id('input_value')
	x = x_element.text
	y = calc(x)
	# Input answer and submit
	answer = browser.find_element_by_id('answer')
	answer.send_keys(y)
	button_submit = browser.find_element_by_css_selector('button.btn')
	button_submit.click()

finally:
	time.sleep(15)
	browser.quit()