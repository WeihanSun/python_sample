# print and exception

import datetime

# exception
def exception_test(a, b):
    print(u'＝＝＝＝計算開始＝＝＝＝')
    result = 0
    try:
        result = a + b
    except:
        print(u'(2)計算出来ませんでした！')
        raise  # throw out error to the calling place
    finally:
        print(u'(2)計算終了')
    return result


# exception
try:
    exception_test('1', 2)
except:
    print('(1)エラーを受け取りました')

# print no return
print('hello,', end='')  # no return
print(' python')

# print format
print(u'Hello, %s' % 'Andy')
today = datetime.date.today()
print(u'Today is %d/%d/%d' % (today.year, today.month, today.day))  # use %
print(u'Today is {2}-{1}-{0}'.format(today.year, today.month, today.day))  # use format

# 'is' is to compare id(obj)
# == is to compare values of same type of objects
val = None
test_list_1 = [100, 200, 300]  # == is overloaded by list
test_list_2 = [100, 200, 300]
print(test_list_1 == test_list_2)
print(test_list_1 is test_list_2)  # False, different id
print(id(val) == id(None))
print(val is None)
print(val == None)





