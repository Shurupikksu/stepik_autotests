from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)

	price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	button_book = browser.find_element(By.ID, "book")
	button_book.click()
	# Calc X
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	# Input answer
	answer = browser.find_element(By.ID, "answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
	answer.send_keys(y)
	button_submit = browser.find_element(By.ID, "solve")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
	button_submit.click()

finally:
	time.sleep(10)
	browser.quit()

