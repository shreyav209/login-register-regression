# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager





# @pytest.fixture(scope='class',params=['edge','chrome','firefox'])
# def browser_setup(request):
#     options = Options()
#     service = Service(EdgeChromiumDriverManager().install())    
#     driver = webdriver.Edge(service=service, options=options)
#     driver.maximize_window()
#     urls ={
#             "register": "https://demoqa.com/register",
#             "login": "https://demoqa.com/login",
#             "practiceform": "https://demoqa.com/automation-practice-form"

#     }
#     request.cls.driver = driver
#     request.cls.urls = urls
#     driver.implicitly_wait(5)
#     yield
#     driver.close()


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#Run tests at different browsers using specific browser via command linte --browser parameter

#This function is used to add command-line options to Pytest. 
#The --browser option allows you to specify which browser to use for the test run.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge")


@pytest.fixture(scope="class")
def browser_setup(request):
#Retrieves the value of the --browser option passed from the command line.
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.maximize_window()

    #Define multiple URLs in a list or dictionary within your fixture. 
    #The fixture will initialize the WebDriver and navigate to the desired URL based on the tests requirement.
    urls = {
        "register": "https://demoqa.com/register",
        "login": "https://demoqa.com/login",
        "practiceform": "https://demoqa.com/automation-practice-form"
    }
    
    request.cls.driver = driver
    request.cls.urls = urls
    driver.implicitly_wait(5)
    
    yield driver
    
    driver.quit()
