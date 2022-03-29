from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SetUpDriver:

    @staticmethod
    def __set_options():
        print("        4.2.1) Creating an options instance of ChromeOptions class for webdriver.")
        options = webdriver.ChromeOptions()
        print("        4.2.2) Trying to get the Chrome Profile path.")
        with open("../../necessaryData/chromeProfilePath/path", "r") as cppath:
            chrome_profile_path = cppath.read()
        print("        4.2.3) Chrome Profile path was gotten successfully.")
        print("        4.2.4) Setting up all the necessary chrome options.")
        options.add_argument(f"user-data-dir={chrome_profile_path}")
        options.add_argument(f"--window-size=800,600")
        options.add_argument("--incognito")
        options.add_argument("--disable-blink-features=AutomationControlled")
        print("        4.2.4) All the options are set up.")
        return options

    @classmethod
    def driver_constructor(cls):
        print("4. RUNNING CHROME DRIVER CONSTRUCTOR:")
        print("    4.1) Setting path to executable chromedriver.")
        print("    4.2) Setting Chrome Options for webdriver:")
        driver = webdriver.Chrome(
            service=Service(executable_path=f"../../necessaryData/chromedriver/chromedriver"),
            options=cls.__set_options()
        )
        print("    4.3) Driver instance created successfully.\n")
        return driver
