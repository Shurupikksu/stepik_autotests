import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
	def test_success(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_css_selector('[placeholder = "Input your first name"]')
		input1.send_keys("Иван")
		input2 = browser.find_element_by_css_selector('[placeholder = "Input your last name"]')
		input2.send_keys("Иванов")
		input3 = browser.find_element_by_css_selector('[placeholder = "Input your email"]')
		input3.send_keys("Test@mail.ru")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed/another text")
		time.sleep(10)
		browser.quit()

	def test_failuer(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_css_selector('[placeholder = "Input your first name"]')
		input1.send_keys("Иван")
		input2 = browser.find_element_by_css_selector('[placeholder = "Input your last name"]')
		input2.send_keys("Иванов")
		input3 = browser.find_element_by_css_selector('[placeholder = "Input your email"]')
		input3.send_keys("Test@mail.ru")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		time.sleep(1)
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed/another text")
		time.sleep(10)
		browser.quit()

if __name__ == "__main__":
    unittest.main()