# functions
# customer's package


def func1(*args):
    print(type(args))
    print(len(args))


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

if __name__ == '__main__':
    func1(1, 2, 3, 4, 5)
    func2(1, 2, 3, 4, 5)
    func3(1, 2, 3, 4, 5, name='fun3', num=2)
    func3(1, 2, 3, name='new1', num=2, unknown=False)

# customer's package
import sys
sys.path.append('./packages/test_p')
import packages.test_p.calc
print(packages.test_p.calc.plus_value(3, 4))


from packages.test_p.calc import plus_value
print(plus_value(1,2))

from packages.test_p.calc import testClass
print(testClass.multiply_value(2, 3))


