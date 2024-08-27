import pytest,time
from login_pages import LoginPage

#test data
username = 'Text0012'
password = 'Text@001'

username1 = 'Text00'
password1 = 'Text@00'


@pytest.mark.usefixtures('browser_setup')  #browser invocation fixture is called
class TestLogin:

    def test_valid_login(self):
        #access these URLs using self.urls and navigate to the desired page using driver.get().
        self.driver.get(self.urls["login"])
        loginpage = LoginPage(self.driver)
        time.sleep(3)
        loginpage.getUsername(username)
        loginpage.getPassword(password)
        time.sleep(3)
        loginpage.do_login()
        time.sleep(5)
        assert loginpage.getSuccessMessage() == username
        loginpage.doLogout()

    def test_invalid_login(self):
        self.driver.get(self.urls["login"])
        loginpage = LoginPage(self.driver)
        time.sleep(3)
        loginpage.getUsername(username1)
        loginpage.getPassword(password1)
        time.sleep(3)
        loginpage.do_login()
        time.sleep(5)
        assert loginpage.getInvalidUserPassword() == 'Invalid username or password!'
        # loginpage.doLogout()


