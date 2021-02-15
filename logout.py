class Logout():

    def __init__(self, driver):
        self.driver = driver

        self.dropdown_xpath = "//img[@class='demo-avatar whiteBgColor']"

        self.logout_btn_xpath = "//span[contains(text(),'Logout')]"

    def click_dropdown(self):
        self.driver.find_element_by_xpath(self.dropdown_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_btn_xpath).click()
