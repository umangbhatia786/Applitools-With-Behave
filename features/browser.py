from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.utils import ChromeType

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from applitools.selenium import Eyes
from features.resources.test_config.my_config import *

dir_path = os.getcwd()

chrome_driver_path_used = dir_path + r'/features/resources/drivers/chromedriver.exe'
gecko_driver_path_used = dir_path + r'/features/resources/drivers/geckodriver.exe'


class Browser(object):

    if BROWSER == 'CHROME':
        print(chrome_driver_path_used)
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif BROWSER == 'FIREFOX':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif BROWSER == 'BRAVE':
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

    driver.implicitly_wait(20)
    driver.set_page_load_timeout(30)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get(APP_UNDER_TEST)

    def closeBrowser(context):
        context.driver.close()
        context.driver.quit()
        # self.driver.quit()


