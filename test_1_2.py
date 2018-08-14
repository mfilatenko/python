from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get("http://slotmachinescript.com/")
browser.maximize_window()

#Test 1: Play one round (“SPIN” button). Wait until the round is finished.
print ("*** RUNNING 1st TEST ***")
click_spin = browser.find_element_by_xpath('//*[@id="spinButton"]').click()
element = WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'disabled')))

#Test 2: Change the “BET” by 2 points, play the round and check the “TOTAL SPINS”.
print ("*** RUNNING 2nd TEST ***")

def up_bet(arg):
	for bet in range(arg):
		browser.find_element_by_xpath('//*[@id="betSpinUp"]').click()
up_bet(2)

click_spin = browser.find_element_by_xpath('//*[@id="spinButton"]').click()	
result = browser.find_element_by_xpath('//*[@id="credits"]').text
bet = browser.find_element_by_xpath('//*[@id="bet"]').text
print ("Your bet =", bet)
print ("Total spins =", result)



	
	
		