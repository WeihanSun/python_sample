# functions
# customer's package
# lambda function (no function name)
# yield function (use next(), use less memory)
# callable: check function callable


def func1(*args):
    print(type(args))
    print(len(args))

# yield function
def func_y():
    yield(u'H1')
    yield (u'H2')
    yield (u'H3')

# args: list
def func2(must1, must2, *args):
    print(len(args))


# p2: list
# p3: dict
def func3(p1, *p2, **p3):
    print(type(p2))
    print(p2)
    print(type(p3))
    print(p3)
    print(type(p3['name']))
    print(type(p3['num']))
    print('unknown' in p3)

# dict only
def func4(**p4):
    print(p4)
    print(p4['name'])

if __name__ == '__main__':
    func1(1, 2, 3, 4, 5)
    func2(1, 2, 3, 4, 5)
    func3(1, 2, 3, 4, 5, name='fun3', num=2)
    func3(1, 2, 3, name='new1', num=2, unknown=False)
    func4(name='p4', num=2)

# customer's package
import sys
sys.path.append('./packages/test_p')
import packages.test_p.calc
print(packages.test_p.calc.plus_value(3, 4))
from packages.test_p.calc import plus_value
print(plus_value(1,2))
from packages.test_p.calc import testClass
print(testClass.multiply_value(2, 3))

# lambda function
fun_l = lambda num_1, num_2 : num_1 + num_2
print(fun_l(10, 100))

# yield function
f = func_y()
for i in func_y():
    print(i)
print(next(f))
print(next(f))
print(next(f))

# yield generator
gen_sample = (i for i in u'おはよう こんにちは こんばんは'.split())
print(gen_sample)
for i in gen_sample:
    print(i)

# function callable
print(callable(fun_l))
print(callable(func_y))

