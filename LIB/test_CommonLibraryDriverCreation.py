import unittest
from selenium import webdriver
import os
import json

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print basedir
filename = os.path.join(basedir + '\\CONFIG\\commonconfig.json')
with open(filename,"r") as f:
    config_json = json.load(f)

class test_CommonLibraryDriverCreation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.get(config_json["UIDetails"]["jquerywebsite"])
        # self.driver.get(config_json["UIDetails"]["jquerywebsite"])


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()