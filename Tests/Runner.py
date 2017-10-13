import pytest
import Runner

@pytest.fixture
def webCrawler():
    return Runner.WebCrawler()

def test_is_chrome_open(webCrawler):
    assert webCrawler.GetDriverStatus() == True

def test_is_chrome_close(webCrawler):
    webCrawler.CloseDriver()
    assert webCrawler.GetDriverStatus() == False