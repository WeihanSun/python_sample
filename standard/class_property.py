# class property
# There are 2 formats

from _datetime import datetime


class ContextManager:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True


# format 1
class TestClass1:
    def __init__(self, year, month, date):
        self.yy = year
        self.mm = month
        self.dd = date
        self.tmp = date

    def get_date(self):
        return u'%s/%s/%s' % (self.yy, self.mm, self.dd)

    date_str = property(get_date)

    def get_tmp(self):
        return self.tmp

    def set_tmp(self, d):
        self.tmp = d

    temp = property(set_tmp, get_tmp)  # use property() to bind property to a var


# format 2
class TestClass2:
    def __init__(self, year, month, date):
        self.yy = year
        self.mm = month
        self.dd = date

    @property
    def date_str(self):  # now date_str is created with property
        return u'%s/%s/%s' % (self.yy, self.mm, self.dd)

    @property
    def date_val_str(self):
        return u'%s/%s/%s' % (self.yy, self.mm, self.dd)

    @date_val_str.setter
    def date_val_str(self, tmp):
        self.date_val_str = tmp

    @date_val_str.deleter
    def date_val_str(self):
        del self.date_val_str


today = datetime.today()
class1 = TestClass1(today.year, today.month, today.day)
with ContextManager():
    print(class1.date_str)
    class1.date_str = '2019/09/09'  # no setter so error
class1.tmp = 10  # no problem because it has setter

print('------------------------')
class2 = TestClass2(today.year, today.month, today.day)
with ContextManager():
    class2.dd = 10
    print(class2.date_str)

with ContextManager():
    class2.dd = 20
    print(class2.date_val_str)
    class2.date_val_str = "changed"
    print(class2.date_val_str)
    del class2.date_val_str
    print(class2.date_val_str)
