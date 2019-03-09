import pytest
from Utils.Constants import *
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in Your Browser Name e.g chrome, Firefox")
@pytest.fixture(scope='class')
def test_set_up(request):
    import os
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        proj_path = os.getcwd()
        driver_path = proj_path.replace("\\", "/") + "/Drivers"
        print(driver_path)
        driver = webdriver.Chrome(executable_path=driver_path + "/chromedriver.exe")
    elif browser == "firefox":
        proj_path = os.getcwd()
        driver_path = proj_path.replace("\\", "/") + "/Drivers"
        print(driver_path)
        driver = webdriver.Chrome(executable_path=driver_path + "/geckodriver.exe")
    driver.get(URL)
    driver.maximize_window()
    driver.implicitly_wait(30)

    request.cls.driver = driver
    yield
    driver.quit()