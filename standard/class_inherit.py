# class inherit
# call parent's method
# instance method, class method,

import time


# base class
class Country:
    num_in_earth = 157  # class value

    def __init__(self, country_name):
        self.country_name = country_name

    def get_name(self):
        return self.country_name

    @classmethod
    def get_country_time(cls, time_area=0):
        t = time.gmtime()
        return u'Today is %d/%d/%d %d:%d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour + time_area, t.tm_min)


# child class
class City(Country):
    def __init__(self, country_name, city_name):
        super().__init__(country_name)  # the same to blow
        # super(City, self).__init__(country_name)
        self.city_name = city_name

    # To call parent's method
    # (1) hard call (parent's name)
    # (2) super()
    def get_name(self):
        return self.city_name + '@' + super().get_name()
        # return self.city_name + '@' + super(City, self).get_name()
        # return self.city_name + '@' + Country.get_name(self)


classes = list([])
classes.append(City('Japan', 'Tokyo'))
classes.append(City('USA', 'Washington, D.C.'))

for cls in classes:
    print("===== Class =====")
    print('country_name --> ' + cls.country_name)
    print('city_name --> ' + cls.city_name)
    print(cls.get_name())
# call class method
print(Country.get_country_time(9))  # Japanese time area is east 9
# access class value
print(u"There are %d countries in the world now." % Country.num_in_earth)
