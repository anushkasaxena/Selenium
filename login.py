class Login():
    def __init__(self, driver):
        self.driver = driver
        self.signin_btn_link_text = "Sign In"
        self.username_textbox_id = "luser"
        self.password_textbox_id = "password"
        self.login_btn_xpath = "//button[@class='btn btn-green signin-button']"
        self.porfile_dropdown_xpaath = "//div[@class='header-main__profile']//img"
        self.myprofile_xpath = "//a[@class='remove-anchor__decoration']//span[contains(text(),'My Profile')]"
        self.basic_xpath = "//nav[@class='demo-navigation mdl-navigation']//a[1]"


    def click_sigin(self):
        self.driver.find_element_by_link_text(self.signin_btn_link_text).click()

    def enter_user_name(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()

    def enter_my_profile(self):
        self.driver.find_element_by_xpath(self.porfile_dropdown_xpaath).click()

    def click_myprofile_path(self):
        self.driver.find_element_by_xpath(self.myprofile_xpath).click()

    def click_basic(self):
        self.driver.find_element_by_xpath(self.basic_xpath).click()

