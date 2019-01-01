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

class draganddrop(test_CommonLibraryDriverCreation,unittest.TestCase,GenericUIFunction):

    @pytest.mark.skip("Dont want to Execute")

    def test_drag_drop(self):
        self.driver.get(config_json["UIDetails"]["jquerywebsite"])

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
    @pytest.mark.skip("Dont want to Execute")

    def test_switch_to_window(self):
        self.driver.get(config_json["UIDetails"]["jquerywebsite"])
        self.driver.maximize_window()
        print "Google is Opened"
        self.driver.execute_script("window.open('http://www.google.com/','New Window')")
        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.get("http://www.google.com/")
        self.driver.execute_script("window.open('http://www.facebook.com/','New Window')")
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.get("http://www.facebook.com/")
        self.driver.execute_script("window.open('http://www.amazon.com/','New Window')")
        self.driver.switch_to_window(self.driver.window_handles[2])
        self.driver.get("http://www.amazon.com/")
        time.sleep(5)
    @pytest.mark.skip("Dont want to Execute")

    def test_window_popup(self):
        self.driver.get("https://www.hdfcbank.com/")
        self.driver.maximize_window()
        print "HDFC website has been opened"
        mainwindowid = self.driver.current_window_handle
        self.ClickElement("//a[@class='homeloginbtn']")
        print self.driver.current_window_handle
        for handle in self.driver.window_handles:
            print "handles are", handle
            if handle != mainwindowid:
                popupwindowid = handle
                print "popupwindowid", popupwindowid
                self.driver.switch_to_window(popupwindowid)
                self.ClickElement("//div[@class='container']/div[@class='pdtb25 text-center']/a[contains(text(),'Continue to NetBanking')]")

        time.sleep(5)

    def test_alert_window(self):
        self.driver.get("https://www.rediff.com/")
        self.driver.maximize_window()
        self.WaitUntilElementFound("//u[contains(text(),'rediff')]")
        self.ClickElement("//u[contains(text(),'rediff')]")
        self.WaitUntilElementFound("//input[@name='proceed']")
        self.ClickElement("//input[@name='proceed']")
        alert = self.driver.switch_to_alert()
        print alert.text
        time.sleep(10)
        alert.accept()

        time.sleep(10)



