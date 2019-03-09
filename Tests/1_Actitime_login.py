import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/login.do")

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_xpath("//*[text()='Login ']").click()

time.sleep(3)

driver.find_element_by_xpath("//*[text()='Logout']").click()

driver.quit()