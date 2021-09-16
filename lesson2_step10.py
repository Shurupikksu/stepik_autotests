from selenium import webdriver
import math
import time

# Math formula
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	# Catch X 
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	# Input answer
	input_answer = browser.find_element_by_id("answer")
	input_answer.send_keys(y)
	# Select checkbox and radiobutton
	check = browser.find_element_by_id("robotCheckbox")
	browser.execute_script("return arguments[0].scrollIntoView(true);", check)
	check.click()
	radio = browser.find_element_by_id("robotsRule")
	radio.click()
	# Scroll to button submit
	button = browser.find_element_by_css_selector("button.btn")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

finally:
	time.sleep(15)
	browser.quit()
