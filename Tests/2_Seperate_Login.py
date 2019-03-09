import time
from selenium import webdriver

import os

def launch():
    global driver
    driver_path = (os.getcwd().replace("Tests", "").replace("\\", "/") + "Drivers" + "/chromedriver.exe")
    driver = webdriver.Chrome(executable_path=driver_path)
    print(driver_path)
    driver.get("http://localhost/login.do")
    driver.maximize_window()
    driver.implicitly_wait(30)

def login():
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_xpath("//*[text()='Login ']").click()

def logout():
    driver.find_element_by_id("logoutLink").click()
    time.sleep(3)
    driver.quit()

launch()
login()
logout()