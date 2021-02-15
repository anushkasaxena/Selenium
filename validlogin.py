class ValidLogin():
    def __init__(self, driver):
        self.driver = driver

        self.name_xpath = "//div[@class='mdl-cell mdl-cell--9-col mdl-cell--12-col-phone textBold medText']"
        self.institue_name_xpath = "//div[contains(text(),'geu')]"
        self.emailid_xpath = "//div[contains(text(),'shkanushka@gmail.com')]"

    def get_name(self):
        a = self.driver.find_element_by_xpath(self.name_xpath).text
        return a

    def get_institue_name(self):
        a = self.driver.find_element_by_xpath(self.institue_name_xpath).text
        return a

    def get_emailid(self):
        a = self.driver.find_element_by_xpath(self.emailid_xpath).text
        return a


