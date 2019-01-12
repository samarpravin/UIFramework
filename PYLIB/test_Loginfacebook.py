from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import json
import re
import unittest
import time
from LIB.test_CommonLibraryDriverCreation import test_CommonLibraryDriverCreation
from BIN.GenericUIFunction import GenericUIFunction
import os
import pytest

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print basedir

filename = os.path.join(basedir + '\\CONFIG\\commonconfig.json')


with open(filename,"r") as f:
    config_json = json.load(f)

class test_login_facebook(test_CommonLibraryDriverCreation,GenericUIFunction,unittest.TestCase):
    def test_signupFacebook(self):
        self.driver.get(config_json["UIDetails"]["facebook"])
        self.driver.maximize_window()
        self.WaitUntilElementFound(config_json["XPATHFB"]["firstName"])
        self.InputElement(config_json["XPATHFB"]["firstName"],"PK")
        self.InputElement(config_json["XPATHFB"]["lastName"],"SAMAR")
        self.InputElement(config_json["XPATHFB"]["registration"],"3537457")
        self.InputElement(config_json["XPATHFB"]["newPassword"],"hari")
        self.SelectElement(config_json["XPATHFB"]["dayselect"],"16")
        self.SelectElement(config_json["XPATHFB"]["monthselect"],"Oct")
        self.SelectElement(config_json["XPATHFB"]["yearselect"],"2011")
        self.ClickElement(config_json["XPATHFB"]["Gender"])
        time.sleep(30)






if __name__ == "__main__":
    unittest.main()