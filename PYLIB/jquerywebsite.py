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

fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir
filename = os.path.join(fileDir, '../CONFIG/commonconfig.json')
with open(filename,"r") as f:

# with open("C:\Users\pravin\PycharmProjects\Framework_Genric\CONFIG\commonconfig.json",
#           "r") as f:
    config_json = json.load(f)

class Dropdown(test_CommonLibraryDriverCreation,unittest.TestCase,GenericUIFunction):

    def test_drag_drop(self):
        self.driver.maximize_window()
        self.WaitUntilElementFound("//a[contains(text(),'Droppable')]")
        time.sleep(5)
        self.ClickElement("//a[contains(text(),'Droppable')]")
        actionchains = ActionChains(self.driver)
        frame=self.driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        self.driver.switch_to_frame(frame)
        self.WaitUntilElementFound("//div[@id='draggable']")
        draggable = self.driver.find_element_by_xpath("//div[@id='draggable']")
        droppable = self.driver.find_element_by_xpath("//div[@id='droppable']")
        time.sleep(6)
        actionchains.context_click(draggable)
        time.sleep(4)
        actionchains.drag_and_drop(draggable,droppable).perform()
        time.sleep(4)

        self.driver.switch_to.default_content() #it will switch to main window
        time.sleep(2)
        self.ClickElement("//a[contains(text(),'Draggable')]")

        time.sleep(30)


