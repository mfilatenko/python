from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://rozetka.com.ua") #открыть сайт

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/div[1]/div[1]/header/div/div[2]/div[2]/form/div/div[1]/input')))#дождаться кликабельности поиска
search = browser.find_element_by_xpath('/html/body/app-root/div/div[1]/div[1]/header/div/div[2]/div[2]/form/div/div[1]/input')

search.send_keys("iPhone 6") #ввод слова для поиска
enter_search = browser.find_element_by_xpath("/html/body/app-root/div/div[1]/div[1]/header/div/div[2]/div[2]/form/button")
enter_search.click() #нажать кнопку поиск

result = browser.find_elements_by_id('block_with_goods')
for i in result:
	print (i.text)
	if "iPhone" in i.text:
		print ("\n Test Passed \n")
		print (i.text)
		print ("\n Test Passed \n")
	else:
		print ("Test Failed") 
		print (i.text)


