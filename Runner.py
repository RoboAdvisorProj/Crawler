from selenium import webdriver
from Utils import LogManager
from Setting import DefineManager

class WebCrawler(object):
    def __init__(self):
        LogManager.PrintLogMessage("WebCrawler", "__init__", "open chrome browser", DefineManager.LOG_LEVEL_INFO)
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1920x1080')
            options.add_argument("disable-gpu")

            self.driver = webdriver.Chrome(chrome_options=options)
            self.driverStatus = True
        except:
            LogManager.PrintLogMessage("WebCrawler", "__init__", "cannot open chrome browser", DefineManager.LOG_LEVEL_ERROR)
            self.driverStatus = False

    def GetDriverStatus(self):
        return self.driverStatus

    def TakePicture(self, url):
        if self.driverStatus == False:
            LogManager.PrintLogMessage("WebCrawler", "TakePicture", "chrome browser not working", DefineManager.LOG_LEVEL_WARN)
            return False
        LogManager.PrintLogMessage("WebCrawler", "TakePicture", "taking shot screen url: " + url, DefineManager.LOG_LEVEL_INFO)
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        self.driver.get_screenshot_as_file("../Src/test.png")
        return True

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
