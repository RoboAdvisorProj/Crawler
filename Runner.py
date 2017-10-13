from selenium import webdriver
from Utils import LogManager
from Setting import DefineManager

class WebCrawler(object):
    def __init__(self):
        LogManager.PrintLogMessage("WebCrawler", "__init__", "open chrome browser", DefineManager.LOG_LEVEL_INFO)
        try:
            self.driver = webdriver.Chrome()
            self.driverStatus = True
        except:
            LogManager.PrintLogMessage("WebCrawler", "__init__", "cannot open chrome browser", DefineManager.LOG_LEVEL_ERROR)
            self.driverStatus = False

    def GetDriverStatus(self):
        return self.driverStatus

    def CloseDriver(self):
        LogManager.PrintLogMessage("WebCrawler", "CloseDriver", "close chrome browser", DefineManager.LOG_LEVEL_INFO)
        try:
            self.driver.quit()
            self.driverStatus = False
        except:
            LogManager.PrintLogMessage("WebCrawler", "CloseDriver", "cannot close chrome browser", DefineManager.LOG_LEVEL_ERROR)
            self.driverStatus = True

    def __del__(self):
        return
