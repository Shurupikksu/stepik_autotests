import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
	print("\nStart browser")
	browser = webdriver.Chrome()
	yield browser
	print("\nQuit browser")
	browser.quit()

@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_different_links(browser, links):
	link = f"https://stepik.org/lesson/{links}/step/1"
	browser.get(link)
	browser.implicitly_wait(7)
	textarea = browser.find_element(By.TAG_NAME, "textarea")
	textarea.send_keys(str(math.log(int(time.time()))))
	button_submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
	button_submit.click()
	message_area = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
	message = message_area.text
	assert message == 'Correct!', \
	f"wrong message, got {message}"
