from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.binance.com/register.html")

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-form"]/div[8]/p/a')))
# Go to Log In screen
log_in = browser.find_element_by_xpath('//*[@id="register-form"]/div[8]/p/a').click()

# Input e-mail
mail = browser.find_element_by_xpath('//*[@id="email"]')
mail.send_keys("maksim@ukr.net") #Enter e-mail

# Input password
password = browser.find_element_by_xpath('//*[@id="pwd"]')
password.send_keys("maksim") #Enter Password

#Press Log in button
button = browser.find_element_by_xpath('//*[@id="login-btn"]')
if button.is_enabled():
	button.click()
	print ("LogIn successful! Welcome!")
else:
	print ("'Log In' button is not available. Observe warning message!")