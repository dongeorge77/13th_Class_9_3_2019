class CreateUser:
    def __init__(self,driver):
        self.driver=driver

        self.clk_users_btn="//*[text()='USERS']"

        self.add_nw_usr_btn="//*[text()='Add User']"  #"usersManagementBodyTagId"

        self.frst_name="//*[@id='userDataLightBox_firstNameField']"

        self.lst_name="//*[@id='userDataLightBox_lastNameField']"

        self.enter_email="//*[@id='userDataLightBox_emailField']"

        self.user_name="userDataLightBox_usernameField"

        self.frst_pwd="userDataLightBox_passwordField"

        self.pwd_cnfrm="userDataLightBox_passwordCopyField"

        self.clk_create_btn="//*[text()='Create User']"





    def click_on_users_tab(self):
        self.driver.find_element_by_xpath(self.clk_users_btn).click()

    def new_user(self):
        self.driver.find_element_by_xpath(self.add_nw_usr_btn).click()
        #self.driver.find_element_by_id(self.add_nw_usr_btn).click()

    def firstname(self):
        self.driver.find_element_by_xpath(self.frst_name).send_keys("unknown")

    def lastname(self):
        self.driver.find_element_by_xpath(self.lst_name).send_keys("name")

    def email(self):
        self.driver.find_element_by_xpath(self.enter_email).send_keys("unknownname@email.com")

    def username(self):
        self.driver.find_element_by_id(self.user_name).send_keys("UnknownNewUser")

    def password(self):
        self.driver.find_element_by_id(self.frst_pwd).send_keys("123456")

    def confirm_password(self):
        self.driver.find_element_by_id(self.pwd_cnfrm).send_keys("123456")

    def create_button(self):
        self.driver.find_element_by_xpath(self.clk_create_btn).click()
