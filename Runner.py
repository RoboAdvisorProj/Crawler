from selenium import webdriver
from Utils import LogManager
from Setting import DefineManager
from Tests import Runner

class WebCrawler:
    def __init__(self):
        LogManager.PrintLogMessage("WebCrawler", "__init__", "open chrome brower", DefineManager.LOG_LEVEL_INFO)
        self.driver = webdriver.Chrome()

    def __del__(self):
        LogManager.PrintLogMessage("WebCrawler", "__del__", "close chrome brower", DefineManager.LOG_LEVEL_INFO)
        self.driver.quit()


crawler = WebCrawler()