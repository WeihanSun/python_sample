
# context manager
# (use 'with' to brace a block of processing, where is added prefix and suffix processing)
# there are 2 methods, one is to define a class with __enter__, __exit__
# the other is to use @contextmanager to define a function (use yield to divide the prefix an suffix)

from contextlib import contextmanager  # to use decoder @contextmanager


# class with context manager
# define __enter__(), __exit__()
class ContextManagerTest:
    def __enter__(self):  # prefix method
        print('__enter__')
        return 'as obj'  # return to as

    def __exit__(self, exc_type, exc_val, exc_tb):  # suffix method
        print('__exit__')
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True


# context manager function
@contextmanager
def context_manager_func():
    print('..enter..')
    yield
    print('..exit..')


# Context manager
# class type
with ContextManagerTest() as as_obj:
    print("within class context?")
    val = int('abc')
print(as_obj)
print('------------------')
# function type
with context_manager_func():
    print('within context manager')

