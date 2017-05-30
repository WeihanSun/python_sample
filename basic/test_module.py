# test module
# only class


class TestClass:
    def __init__(self):
        self.name = 'test_module.test_class'
        pass

    def get_name(self):
        return self.name


class Country:
    def __init__(self, country_name=''):
        self.country_name = country_name

    def __eq__(self, other):
        if self.country_name == other.country_name:
            print('Same country')
            return True
        else:
            print('Different Country')
            return False


class City(Country):
    def __init__(self, country_name, city_name):
        super().__init__(country_name)
        self.city_name = city_name






