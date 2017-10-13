import pytest
import Runner
from . import Weather

@pytest.fixture
def webCrawler():
    return Runner.WebCrawler()

def test_is_chrome_open(webCrawler):
    assert webCrawler.GetDriverStatus() == True

def test_is_chrome_close(webCrawler):
    webCrawler.CloseDriver()
    assert webCrawler.GetDriverStatus() == False

def test_take_screen_shot(webCrawler):
    assert webCrawler.TakePicture("http://openweathermap.org/city/1835848") == True

def test_get_today_weather(webCrawler):
    todayWeather = Weather.GetTodayWeather(webCrawler)
    assert todayWeather != None