from selenium import webdriver

class WebCrawler:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.quit()

crawler = WebCrawler()