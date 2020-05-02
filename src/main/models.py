class Location:
    def __init__(self, city, lon, lat):
        self.__city = city
        self.__lon = lon
        self.__lat = lat

    def city(self):
        return self.__city

    def lon(self):
        return self.__lon

    def lat(self):
        return self.__lat


class WeatherDetails:
    __URL = 'https://www.metaweather.com/static/img/weather/{}.svg'

    def __init__(self, weather, abbr):
        self.__weather = weather
        self.__abbr = abbr

    def weather(self):
        return self.__weather

    def get_image(self):
        return self.__URL.format(self.__abbr)
