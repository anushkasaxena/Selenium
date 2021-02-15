from selenium import webdriver
import time
import unittest
from login import Login
from validlogin import ValidLogin
from logout import Logout
from search import Search
import HtmlTestRunner

class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome("chromedriver.exe")
        cls.driver.get("https://www.geeksforgeeks.org/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_login(self):
        l = Login(self.driver)
        l.click_sigin()
        time.sleep(10)
        l.enter_user_name("shkanushka@gmail.com")

        l.enter_password("Automation@68")
        time.sleep(10)
        l.click_login()
        time.sleep(10)
        l.enter_my_profile()
        l.click_myprofile_path()
        time.sleep(10)
        l.click_basic()

    def test_02_check_name(self):
        validlogin = ValidLogin(self.driver)
        name = validlogin.get_name()
        print('############ Name ##########')
        print(name)
        self.assertEqual(name, "Anu")

    def test_03_check_intitue_name(self):
        validlogin = ValidLogin(self.driver)
        institue = validlogin.get_institue_name()
        print('########### college name ##############')
        print(institue)

        self.assertEqual(institue, "geu")

    def test_04_check_emailid(self):
        validlogin = ValidLogin(self.driver)
        emailid = validlogin.get_emailid()
        print('############ email id ###############')
        print(emailid)

        self.assertEqual(emailid, "shkanushka@gmail.com")
        

    def test_06_logout(self):
        logout = Logout(self.driver)
        logout.click_dropdown()
        logout.click_logout()
        
    def test_06_search(self):
        search = Search(self.driver)
        time.sleep(5)
        search.search_key("c++")
        search.select_key()
        time.sleep(5)
        search.select_link()
        time.sleep(5)

    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/ASUS/.spyder-py3/POMProjectDemo/automation/report'))








