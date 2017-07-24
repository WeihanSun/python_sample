#
# string processing & datetime
#

import datetime
import time

test_str1 = '1234'

print(test_str1.rjust(10, '0'))  # right fill with 0
print(test_str1.ljust(10, '*'))  # left fill with *

test_str2 = 'Python-string'
print(test_str2.find('python'))  # -1: no found
print(test_str2.find('string'))  # return the position
print(test_str2.startswith('string', 7))  # find start string from specified position, True

print(test_str2.upper())
print(test_str2.lower())

print(('     ' + test_str2 + '     ').strip())  # get rid of tab or blank space
print(('prefix-' + test_str2 + '-suffix').lstrip('prefix').rstrip('suffix'))  # get rid of prefix and suffix
print('f{:>05}_{:>03}.bmp'.format(15, 12))  # similar to C

# print time
print(datetime.date.today())
print(datetime.datetime.today())
print(datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S'))
print("tomorrow is " + (datetime.date.today() + datetime.timedelta(days=1)).strftime('%Y/%m/%d'))

# format string
t = time.gmtime()
from datetime import datetime
print(u'GMT: %d/%d/%d %d:%d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min))
print(u'Today is {2}-{1}-{0}'.format(datetime.today().year, datetime.today().month, datetime.today().day))