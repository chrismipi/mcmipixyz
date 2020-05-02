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
