from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.webdriver.support.ui import Select

class GenericUIFunction:

    def ClickElement(self,locator):
        ClickElement = self.driver.find_element_by_xpath(locator)
        ClickElement.click()

    def WaitUntilElementFound(self,locator):
        timeout = 30
        element_present = EC.presence_of_element_located((By.XPATH, locator))
        WebDriverWait(self.driver, timeout).until(element_present)

    def InputElement(self, locator, text):
        password = self.driver.find_element_by_xpath(locator)
        password.send_keys(text)

    def getTextUIElement(self,locator):
        landingpage = self.driver.find_element_by_xpath(locator)
        welcometxt = landingpage.text
        return welcometxt

    def mouse_over(self,locator):
        element_to_hover_over = self.driver.find_element_by_xpath(locator)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def get_matching_xpathcount(self,locator):
        matching_count = self.driver.find_elements_by_xpath(locator)
        len_match_count = len(matching_count) + 1
        return len_match_count

    def SelectElement(self, locator, text):
        Select_element = Select(self.driver.find_element_by_xpath(locator))
        Select_element.select_by_visible_text(text)

    def get_dropdown_values(self,matchingLocator,incrementLocator):
        list = []
        len_match_count = self.get_matching_xpathcount(matchingLocator)
        replace_string = incrementLocator
        for i in range(1, len_match_count):
            replace = re.sub("~", str(i), replace_string)
            GetEelem = self.getTextUIElement(replace)
            print GetEelem
            list.append(GetEelem)
        print list
        return list

    def click_specific_dropdown_value(self,matchingLocator,incrementLocator,UItext):
        list = []
        len_match_count = self.get_matching_xpathcount(matchingLocator)
        replace_string = incrementLocator
        for i in range(1, len_match_count):
            replace = re.sub("~", str(i), replace_string)
            GetEelem = self.getTextUIElement(replace)
            print "GetEelem {}, UItext {}".format(GetEelem,UItext)
            if GetEelem == UItext:
                self.ClickElement(replace)
                print "Successfully Clicked the Element {}".format(GetEelem)
                break

    def login_Amazon(self):
        timeout = 10
        self.driver.maximize_window()
        self.ClickElement("//span[contains(text(),'Hello. Sign in')]")
        self.WaitUntilElementFound("//input[@type='email']")
        email = self.driver.find_element_by_xpath("//input[@type='email']")
        email.send_keys("pravin.kusin@gmail.com")
        continuebutton = self.driver.find_element_by_xpath("//input[@id='continue']")
        continuebutton.click()
        element_present = EC.presence_of_element_located((By.XPATH, "//input[@id='ap_password']"))
        WebDriverWait(self.driver, timeout).until(element_present)
        self.InputElement("//input[@id='ap_password']", "Hari&sadu11")
        # password = self.driver.find_element_by_xpath("//input[@id='ap_password']")
        # password.send_keys("Hari&sadu11")
        login = self.driver.find_element_by_xpath("//input[@id='signInSubmit']")
        login.click()
        element_present = EC.presence_of_element_located(
            (By.XPATH, "//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']"))
        WebDriverWait(self.driver, timeout).until(element_present)
        welcometxt = self.getTextUIElement("//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']")
        # landingpage = self.driver.find_element_by_xpath("//div[@id='nav-tools']/a[1]/span[@class='nav-line-1']")
        # welcometxt =  landingpage.text
        splitvar = welcometxt.split(",")
        if splitvar[0] == "Hello":
            print "login is successfull for the user {}".format(welcometxt)
        else:
            print "login is not successfull for the user {}".format(welcometxt)
            raise Exception




