from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.binance.com/register.html")

#Input login
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
login = browser.find_element_by_xpath('//*[@id="email"]')
login.send_keys("maksim@ukr.net") #Enter login

#Input password
password = browser.find_element_by_xpath('//*[@id="regiterPassword"]')
password.send_keys('maksim') #Enter password

#Repeate password
confirm_pass = browser.find_element_by_xpath('//*[@id="regiterRepeatPassword"]')
confirm_pass.send_keys('maksim7') #repeate password

#Input Referral ID (optional)
referral = browser.find_element_by_xpath('//*[@id="ref"]')
referral.send_keys('') #enter ID

#Checkbox Agree to Binance's
agree = browser.find_element_by_xpath('//*[@id="agreement"]')
if agree.is_enabled():
	agree.click()
else:
	print ("Checkbox not available")
	
#Confirm Regestration
registration = browser.find_element_by_xpath('//*[@id="register-btn"]')
if registration.is_enabled():
	registration.click()
	print ("Registration button selected")
else:
	print ("Registration button is not available")