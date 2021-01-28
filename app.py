from model.loginPage import LoginPage
from model.newPopup import NewPopUp
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="E:/Project/automation/first_user/driver/chromedriver.exe")
driver.maximize_window()
driver.get("https://first-user-dev-dev-ed.my.salesforce.com/")

login = LoginPage(driver)
login.enter_username("first_user_dev.qa@bjitgroup.com")
login.enter_password("bs@devtest20")
login.click_login()

for i in range(204,500):
    driver.get("https://first-user-dev-dev-ed.lightning.force.com/lightning/n/System")
    time.sleep(4)
    newPopup = NewPopUp(driver)
    newPopup.click_new_button()
    time.sleep(2)
    newPopup.Component_item_name("AutoData "+str(i))
    newPopup.Situation()
    newPopup.Account("Test_Account")
    newPopup.save()
    time.sleep(4)
    print("AutoData "+str(i))