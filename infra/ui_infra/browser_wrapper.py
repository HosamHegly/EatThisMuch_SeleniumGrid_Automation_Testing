import json
import time
from os.path import dirname, join
from Utils import cookies
from selenium import webdriver


class BrowserWrapper:
    COOKIE = cookies.cookie

    def __init__(self):
        self.driver = None
        filename = self.get_filename("../../config/config.json")
        with open(filename, 'r') as file:
            self.config = json.load(file)

    #return the webdriver based on the config file options
    def get_driver(self, browser):
        browser_type = self.config["browser"]
        if self.config["grid"]:
            options = self.set_up_capabilities(browser)
            self.driver = webdriver.Remote(command_executor=self.config["hub"], options=options)
            self.driver.fullscreen_window()

        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")  # This line is often necessary in CI environments
            options.add_argument("--disable-dev-shm-usage")  # This can help in environments with
            if browser.lower() == 'chrome':
                self.driver = webdriver.Chrome(options=options)
            elif browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser.lower() == 'edge':
                self.driver = webdriver.Edge()
        url = self.config["url"]

        self.driver.get(url)
        time.sleep(2)
        self.driver.fullscreen_window()

        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.close()
    #return browser capabilities based on the browser
    def set_up_capabilities(self, browser_type):
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
        platform_name = self.config["platform"]
        options.add_argument(f'--platformName={platform_name}')
        return options

    def is_parallel(self):
        return self.parallel

    def close_browser(self):
        if self.driver:
            self.driver.quit()

    def get_browsers(self):
        return self.config["browser_types"]

    def get_filename(self, filename):
        here = dirname(__file__)
        output = join(here, filename)
        return output

    def is_grid(self):
        return self.config['grid']

    def get_browser(self):
        return self.config['browser']
    #add cookies to driver inorder to  skip login
    def add_browser_cookie(self):
        for cookie in self.COOKIE:
            self.driver.add_cookie(cookie)

    def goto(self,url):
        self.driver.get(url)
