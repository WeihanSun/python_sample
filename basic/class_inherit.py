# -*- coding: utf-8 -*-


class Country:

    def __init__(self, country_name):
        self.country_name = country_name


class City(Country):

    def __init__(self, country_name, city_name):
        Country.__init__(self, country_name)
        self.city_name = city_name


classes = list([])
classes.append(City('Japan', 'Tokyo'))
classes.append(City('USA', 'Washington, D.C.'))

for cls in classes:
    print("===== Class =====")
    print('country_name --> ' + cls.country_name)
    print('city_name --> ' + cls.city_name)
