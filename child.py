import traceback


def foo():
    traceback.print_stack()
    pass


def bar():
    foo()
    traceback.print_stack()


def func():
    bar()


def some():
    func()


if __name__ == '__main__':
    some()
