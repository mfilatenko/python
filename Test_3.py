from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get("http://slotmachinescript.com/")
browser.maximize_window()


#Test 3: Play until you win.
print ("*** RUNNING 3rd TEST ***")
print ("*** play until you win ***") 
while True:
	content = browser.find_elements_by_class_name("disabled")	#Spin button while is disable
	win = browser.find_element_by_xpath('//*[@id="lastWin"]').text
	result = browser.find_element_by_xpath('//*[@id="credits"]').text	#print total spins
	if win:
		print ("Last win =", win)
		print ("Total spins =", result)
		if int(result)-(int(start_result)) == int(win):
			print ("Spins added OK")
		else:
			print ("Spins added not OK")
		break
	if content:
		WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="spinButton"]')))
		continue
	else:
		click_spin = browser.find_element_by_xpath('//*[@id="spinButton"]').click()
		start_result = browser.find_element_by_xpath('//*[@id="credits"]').text
		print ("Spins =", start_result)
		