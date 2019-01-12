from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import json
import re
import unittest
from LIB.test_CommonLibraryDriverCreation import test_CommonLibraryDriverCreation
from BIN.GenericUIFunction import GenericUIFunction
import os
import pytest
import sys
import time



basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print basedir
filename = os.path.join(basedir + '\\CONFIG\\commonconfig.json')

with open(filename,"r") as f:

# with open("C:\Users\pravin\PycharmProjects\Framework_Genric\CONFIG\commonconfig.json",
#           "r") as f:
    config_json = json.load(f)

class AmazonLogin(test_CommonLibraryDriverCreation,unittest.TestCase,GenericUIFunction):
    @pytest.mark.skip("Dont want to Execute")
    def test_dropdown_landingpage(self):
        self.driver.get(config_json["UIDetails"]["amazon"])


        self.login_Amazon()
        self.WaitUntilElementFound(config_json["XPATH"]["shopbycataegoryelem"])
        self.mouse_over(config_json["XPATH"]["shopbycataegoryelem"])
        value = self.get_dropdown_values(config_json["XPATH"]["dropdwonlandingpage_count"],config_json["XPATH"]["dropdwonlandingpage_increment"])
        print value
        return value

    def test_dropdown_yourorders(self):
        self.driver.get(config_json["UIDetails"]["amazon"])

        self.login_Amazon()
        self.WaitUntilElementFound(config_json["XPATH"]["yourorderelem"])
        self.mouse_over(config_json["XPATH"]["yourorderelem"])
        value = self.get_dropdown_values(config_json["XPATH"]["yourorders_count"],config_json["XPATH"]["yourorders_increment"])
        print value
        return value

    def test_click_signout(self):
        self.driver.get(config_json["UIDetails"]["amazon"])
        #login
        self.login_Amazon()
        self.WaitUntilElementFound(config_json["XPATH"]["yourorderelem"])
        self.mouse_over(config_json["XPATH"]["yourorderelem"])
        self.click_specific_dropdown_value(config_json["XPATH"]["yourorders_count"],config_json["XPATH"]["yourorders_increment"],"Sign Out")

    def test_Navigate_to_Element_by_Action_Chains(self):
        self.driver.get(config_json["UIDetails"]["amazon"])

        self.login_Amazon()
        self.WaitUntilElementFound("//a[@id='nav-link-shopall']")
        self.mouse_over("//a[@id='nav-link-shopall']")

        self.WaitUntilElementFound("//div[@id='nav-flyout-shopAll']/div[2]/span[1]/span")
        self.mouse_over("//div[@id='nav-flyout-shopAll']/div[2]/span[1]/span")

        self.WaitUntilElementFound("//div[@id='nav-flyout-shopAll']/div[3]/div[1]/div[1]/div/a[1]/span[1]")
        self.ClickElement("//div[@id='nav-flyout-shopAll']/div[3]/div[1]/div[1]/div/a[1]/span[1]")

        action_chains = ActionChains(self.driver)
        self.WaitUntilElementFound("//input[@id='add-to-cart-button']")
        MovetoElem = self.driver.find_element_by_xpath("//input[@id='add-to-cart-button']")
        action_chains.move_to_element(MovetoElem).perform()
        action_chains.click(MovetoElem).perform()



















if __name__ == "__main__":
    unittest.main()





