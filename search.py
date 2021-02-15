class Search():
    def __init__(self, driver):
        self.driver = driver

        self.search_bar_id = "gsc-i-id1"
        self.search_key_xpath = "//body[@class='blog custom-background custom-background-white custom-font-enabled']//tr//tr[1]//td[1]//div[1]//table[1]//tbody[1]//tr[1]//td[1]"

        self.select_link_xpath = "//div[@class='gs-title']//a[@class='gs-title'][contains(text(),'Programming Language - GeeksforGeeks')]"


    def search_key(self, key):
        self.driver.find_element_by_id(self.search_bar_id).clear()
        self.driver.find_element_by_id(self.search_bar_id).send_keys(key)

    def select_key(self):
        self.driver.find_element_by_xpath(self.search_key_xpath).click()

    def select_link(self):
        self.driver.find_element_by_xpath(self.select_link_xpath).click()



