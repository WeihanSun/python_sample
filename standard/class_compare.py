# compare class
# print class

# -*- coding:utf-8 -*-


def key_func(n):
    return n.score


class TestClass:

    def __init__(self, code, name, score):
        self.code = code
        self.name = name
        self.score = score

    # can be printed if define __str__
    def __str__(self):
        return '({}, {}, {})'.format(self.code, self.name, self.score)


l = [
    TestClass(1, 'Python', 100),
    TestClass(2, 'Ruby', 80),
    TestClass(3, 'Perl', 40)
]

print(min(l, key=key_func))
print(max(l, key=key_func))
