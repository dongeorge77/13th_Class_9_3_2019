import time
from selenium import webdriver

from Pages.LoginPage import LoginPage

from Pages.CreateUser import CreateUser

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
        time.sleep(3)

    def test_create_user(self,test_launch_browser):
        cu=CreateUser(driver)
        cu.click_on_users_tab()
        time.sleep(2)
        cu.new_user()
        cu.firstname()
        cu.lastname()
        cu.email()
        cu.username()
        cu.password()
        time.sleep(5)
        cu.confirm_password()
        cu.create_button()

    # def test_logout(self,test_launch_browser):
    #     time.sleep(5)
    #     lg=LogoutPage(driver)
    #     lg.click_on_logout_btn()
    #
    #     driver.quit()
