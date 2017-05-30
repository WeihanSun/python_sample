# functions


def func1(*args):
    print(len(args))

def func2(must1, must2, *args):
    print(len(args))

if __name__ == '__main__':
    func1(1, 2, 3, 4, 5)
    func2(1, 2, 3, 4, 5)
    func2(1, 2)

