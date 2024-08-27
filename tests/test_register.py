import re
import pytest,time
from login_pages import RegisterPage

#test data
firstname = 'Test101'
lastname = 'Test101'
username = 'Test101'
password = 'Test@101'

incorrect_password ='testtt12'


@pytest.mark.usefixtures('browser_setup')  #browser invocation fixture is called
class TestRegister:
    def test_valid_register(self):
        #access these URLs using self.urls and navigate to the desired page using driver.get().
        self.driver.get(self.urls["register"])
        register = RegisterPage(self.driver)
        time.sleep(3)
        register.getFirstName(firstname)
        register.getLastName(lastname)
        register.getUsername(username)
        register.getPassword(password)
        time.sleep(15)
        register.do_register()
        print('<<<< Register >>>>>')
        time.sleep(5)

    def test_user_exists(self):
        #user exists
        self.driver.get(self.urls["register"])
        register = RegisterPage(self.driver)
        time.sleep(3)
        register.getFirstName(firstname)
        register.getLastName(lastname)
        register.getUsername(username)
        register.getPassword(password)
        time.sleep(15)
        register.do_register()
        print('<<<< Register >>>>>')
        assert register.getUserExistsText() == 'User exists!'
        time.sleep(5)


    def test_incorrect_password(self):
        self.driver.get(self.urls["register"])
        register = RegisterPage(self.driver)
        time.sleep(3)
        register.getFirstName(firstname)
        register.getLastName(lastname)
        register.getUsername(username)
        register.getPassword(incorrect_password)
        time.sleep(15)
        register.do_register()
        print('<<<< Register >>>>>')
        assert register.getUserExistsText() == "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer."
        time.sleep(5)


