from selenium.webdriver.common.by import By
import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass:
    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(by_locator)).click()


    def do_send_keys(self,by_locator,text):
            WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).text


class RegisterPage(BaseClass):

    firstName = (By.ID, 'firstname')
    lastName = (By.ID, 'lastname')
    userName = (By.ID, 'userName')
    userPassword = (By.ID, 'password')
    register_btn = (By.ID,'register')
    userExists = (By.ID,'name')

    def __init__(self, driver):
            self.driver = driver

    def getFirstName(self,firstname):
        firstname = self.do_send_keys(self.firstName,firstname)
        return firstname
    
    def getLastName(self,lastname):
        lastname = self.do_send_keys(self.lastName,lastname)
        return lastname

    def getUsername(self,username,):
        username = self.do_send_keys(self.userName,username)
        return username

    def getPassword(self,password):
        password = self.do_send_keys(self.userPassword,password)
        return password

    def do_register(self):
        self.do_click(self.register_btn)

    def getUserExistsText(self):
        print(self.get_element_text(self.userExists))
        return self.get_element_text(self.userExists)
    


class LoginPage(BaseClass):

    username = (By.ID, 'userName')
    password = (By.ID, 'password')
    login_btn = (By.ID, 'login')
    gotologin = (By.ID,'gotologin')
    successMessage_locator  = (By.ID,'userName-value')
    invalid_user_password = (By.ID,'name')
    logout_btn = (By.ID, 'submit')


    def __init__(self, driver):
        self.driver = driver

    def goToBack(self):
        self.do_click(self.gotologin)
    
    def getUsername(self,username,):
        username = self.do_send_keys(self.username,username)
        return username

    def getPassword(self,password):
        password = self.do_send_keys(self.password,password)
        return password

    def do_login(self):
        self.do_click(self.login_btn)

    def getSuccessMessage(self):
        return self.get_element_text(self.successMessage_locator)
    
    def getInvalidUserPassword(self):
        return self.get_element_text(self.invalid_user_password)

    def doLogout(self):
        self.do_click(self.logout_btn)




