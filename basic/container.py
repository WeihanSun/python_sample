#
# duple, list, dict and set
# duple and list have their sequences
# dict and set are arranged automatically

import datetime

# duple is unchangeable, list is changeable
today = datetime.datetime.today()
test_duple = (today.year, today.month, today.day)  # use () and
test_list = [today.year, today.month, today.day]  # use [] and ,
print(test_duple)
print(test_list)

print(test_list.pop(1))
print(test_list)

test_list1 = ['100', '200', '300', '200', '100']
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

