#
# duple, list, dict and set
# duple and list have their sequences
# dict and set are arranged automatically
# list sort reserve zip/zip_longest

# set | & - ^ operation
# set comparison and update

# brace expression

import datetime
import itertools  # itertools.zip_longest
import collections

# duple is unchangeable, list is changeable
today = datetime.datetime.today()
test_duple = (today.year, today.month, today.day)  # use () and
test_list = [today.year, today.month, today.day]  # use [] and ,
print(test_duple)
print(test_list)

print(test_list.pop(1))
print(test_list)

test_list1 = ['100', '200', '300', '200', '100']
print(test_list1)
# sort ascending
test_list1.sort()
#sorted(test_list1)
print(test_list1)
# reserve display
for val in test_list1[::-1]:
    print(val + ' ', end='')
print('')
# reserve list
test_list1.reverse()
#reversed(test_list1)
for index, val in enumerate(test_list1):
    print(u'%d:%s' % (index, val))

print(test_list1.count('100'))  # number of items in list
test_list1 = ['1', '2', '3', '4', '5']
print(test_list1[1:4])  # [start_pos end_pos]
print(test_list1[:2])  # :from the beginning
print(test_list1[2:])  # :to the end
print(test_list1[::2])  # 2 is span
print(test_list1[-2:])  # -1 index from right
print(test_list1[:-1])  #
print(test_list1[::-1])  # opposite side
print('====================')

# dict key:value
test_dict_1 = {'YEAR': test_duple[0], 'MONTH': test_duple[1], 'DAY': test_duple[2]}  # use {}, : and ,
for item in test_dict_1:
    print(item + ':' + str(test_dict_1[item]))
test_dict_1['SECOND'] = today.second  # add item
del(test_dict_1['YEAR'])              # del item
print(test_dict_1)
print('====================')

# set like a hash table no overload and no explicit index
# they can be unified or intersected
# print sequence is following indices of items
test_blank_dic = {}  # this is a blank dictionary
test_set = {'I', 'am', 'a', 'student'}  # use {} and ,
test_set.add('in')
test_set.update({'an', 'Institute', '.'})
print(test_set)
print(test_set.isdisjoint('Institute'))
print(test_set.isdisjoint('University'))
print(test_set.issuperset({'a', 'student', 'in'}))  # supper set
test_set.remove('I')
print(test_set)
print(test_set.issubset({'a', 'student', 'in'}))  # subset
test_set_1 = {'better', 'and', 'better'}  # no overload
print(test_set_1)
print(test_set_1.union(test_set))
print(test_set_1.intersection(test_set))
# also accept operators' operation
print(test_set | {'good'})
print(test_set & {'student', 'in', 'good'})
print(test_set - {'student', 'in'})
print(test_set ^ {'student', 'in', 'good'})  # add item not exist
print('----------------------------')
test_set &= {'student'}
print(test_set)
test_set -= {'good'}
print(test_set)
test_set |= {'I', 'am', 'a'}
print(test_set)
test_set ^= {'in', 'an', 'Institute'}
print(test_set)

# join & split only string elem
l = ['www', 'python-izm', 'com']
str1 = '.'.join(l)  # list
print(str1)
print(str1.split('.'))
str1 = ' '.join('1234567890')  # string
print(str1)
print(str1.split(' '))
str1 = '-'.join({'python': 1, 'izm': 2})  # dic
print(str1)
print(str1.split('-'))

# list loop using zip & zip_longest
item_list = ['desktop', 'laptop', 'tablet', 'smartphone']
stock_list = [12, 83, 55]
price_list = [1.2, 2.0, 0.8, 0.5, 1.7]
# zip loop the shortest time
for item_name, stock_count, price in zip(item_list, stock_list, price_list):
    print(u'{}/{}/{}'.format(item_name, stock_count, price))
# itertools.zip_longest loop the longest time
for item_name, stock_count, price in itertools.zip_longest(item_list, stock_list, price_list):
    print(u'{}/{}/{}'.format(item_name, stock_count, price))

# list all & any
qlist = [0, 1, 2, 3, 4, 5]
print(any(qlist))  # 1 if any 1 in list
print(all(qlist))  # 0 if any 0 in list
print(0 in qlist)

# order dict
test_norm_dict = {}
test_norm_dict['1'] = 1
test_norm_dict['111'] = 111
test_norm_dict['1111'] = 1111
test_norm_dict['11'] = 11
for key in test_norm_dict:
    print(key)
test_order_dict = collections.OrderedDict()
test_order_dict['1'] = 1
test_order_dict['11'] = 11
test_order_dict['111'] = 111
test_order_dict['1111'] = 1111
for key in test_order_dict:
    print(key)

# set comparison
# (1) isdisjoint, issubset <=, issuperset >=
test_set_1 = {'a', 'b', 'c'}
test_set_2 = {'a', 'b', 'c', 'd', 'e'}
print(test_set_1.isdisjoint(test_set_2))
print(test_set_1.issubset(test_set_2))
print(test_set_2.issuperset(test_set_1))
# set calculation without update
# union |, intersection &, difference -, symmetric_difference ^
# with update
# intersection_update &=, difference_update -=, symmetric_difference ^=
test_set_3 = {'a', 'c', 'h'}
print(test_set_1.union(test_set_3))
print(test_set_1)  # not updated
print(test_set_1.intersection(test_set_3))
print(test_set_1.difference(test_set_3))
print(test_set_1.symmetric_difference(test_set_3))

#union_update
test_set_1 |= test_set_3
print(test_set_1)

# brace expression
# list
list_brace = [i*i for i in range(1, 5)]
print(list_brace)
list_brace = [i*4 + j for i in range(0, 5) for j in range(0, 4)]
print(list_brace)
# dict
dict_brace = {i: i for i in range(1,5)}
print(dict_brace)
# set
set_brace = {str(i) for i in range(1,5)}
print(set_brace)
# duple
# yield generator
duple_brace = (i for i in range(1, 5))
print(duple_brace)
