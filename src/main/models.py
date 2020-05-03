class Location:
    def __init__(self, city, lon, lat, country):
        self.__city = city
        self.__lon = lon
        self.__lat = lat
        self.__country = country

    def country(self):
        return self.__country

    def city(self):
        return self.__city

    def lon(self):
        return self.__lon

    def lat(self):
        return self.__lat

    def coordinates(self):
        return '{},{}'.format(self.__lat, self.__lon)


class WeatherDetails:
    __URL = 'https://www.metaweather.com/static/img/weather/{}.svg'

    def __init__(self, weather, abbr):
        self.__weather = weather
        self.__abbr = abbr

    def weather(self):
        return self.__weather

    def get_image(self):
        return self.__URL.format(self.__abbr)


class SiteVisit:
    def __init__(self, ipAddress, coordinates, city, country, platform):
        self.ipAddress = ipAddress
        self.coordinates = coordinates
        self.city = city
        self.country = country
        self.platform = platform
