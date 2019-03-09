import time
from selenium import webdriver

from Pages.LoginPage import LoginPage

from Pages.LogoutPage import LogoutPage

import pytest

class TestLogin:
    @pytest.fixture(scope='class')
    def test_launch_browser(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:/Users/ADMIN/PycharmProjects/13th_Class_9_3_2019/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://localhost/login.do")

    def test_login(self,test_launch_browser):
        lp=LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

    def test_logout(self,test_launch_browser):
        time.sleep(5)
        lg=LogoutPage(driver)
        lg.click_on_logout_btn()

        driver.quit()
