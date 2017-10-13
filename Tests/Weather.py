from Setting import DefineManager
from Utils import LogManager

def GetTodayWeather(webCrawler):

    if webCrawler.SetDriverUrl("http://openweathermap.org/city/1835848") == False:
        return None
    webDriver = webCrawler.GetDriver()
    weatherWidgetClass = webDriver.find_element_by_class_name("weather-widget__main")
    todayWeather = weatherWidgetClass.text
    if todayWeather != None:
        LogManager.PrintLogMessage("Weather", "GetTodayWeather", "today is " + todayWeather, DefineManager.LOG_LEVEL_INFO)
    return todayWeather