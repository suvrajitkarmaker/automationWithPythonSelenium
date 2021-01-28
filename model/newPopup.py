from model.locators import Locators
import time
class NewPopUp():
    def __init__(self, driver):
        self.driver = driver
        
        self.new_button_absXpath = Locators.new_button_absXpath
        self.component_item_name_absXpath = Locators.component_item_name_absXpath
        self.situation_box_absXpath = Locators.situation_box_absXpath
        self.situation_select_absXpath = Locators.situation_select_absXpath
        self.Account_box_absXpath = Locators.Account_box_absXpath
        self.Account_Select_absXpath = Locators.Account_Select_absXpath
        self.save_item_absXpath = Locators.save_item_absXpath
        self.close_new_item = Locators.close_new_item

    def click_new_button(self):
        self.driver.find_element_by_xpath(self.new_button_absXpath).click()

    def Component_item_name(self, value):
        self.driver.find_element_by_xpath(self.component_item_name_absXpath).clear()
        self.driver.find_element_by_xpath(self.component_item_name_absXpath).send_keys(value)
    
    def Situation(self):
        self.driver.find_element_by_xpath(self.situation_box_absXpath).click()
        self.driver.find_element_by_xpath(self.situation_select_absXpath).click()

    def Account(self, value):
        self.driver.find_element_by_xpath(self.Account_box_absXpath).clear()
        self.driver.find_element_by_xpath(self.Account_box_absXpath).send_keys(value)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.Account_Select_absXpath).click()
    def save(self):
        self.driver.find_element_by_xpath(self.save_item_absXpath).click()
        # time.sleep(3)
        # self.driver.find_element_by_xpath(self.close_new_item).click()

