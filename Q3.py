"""Tal Balelty - 312270291"""


def average_io(func):
    """Calculates the average of all function's inputs and outputs so far."""
    average_io.inp = []
    average_io.out = []

    def run(*args):
        average_io.inp.append(args[0])
        ret = func(*args)
        average_io.out.append(ret)
        t = (sum(average_io.inp) / len(average_io.inp), sum(average_io.out) / len(average_io.out))
        print('Average Results: ' + str(t))
        return ret

    return run


def logged(func):
    """Keeps a log of all functions and their parameters that were called."""
    logged.messages = []

    def run(*args, **kwargs):
        ret = func(*args, **kwargs)
        args_param = ''
        kwargs_param = ''
        if args:
            args_param = str(args)
            if kwargs:
                args_param = args_param[:-1] + ', '
                kwargs_param = (', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()])) + ')'
            else:
                args_param = args_param[:-2] + ')'
        elif kwargs:
            kwargs_param = '({})'.format((', '.join(['{}={!r}'.format(k, v) for k, v in kwargs.items()])))
        logged.messages.append("You called {}{}{} it returned {}".format(func.__name__, args_param, kwargs_param, ret))
        for log in logged.messages:
            print(log)
        return ret

    return run


"""Testing functions:"""


@average_io
@logged
def do_nothing_avg(num):
    return num + 2


@logged
def do_nothing2():
    return 9


@logged
def do_nothing1(num, doc, con, my):
    return num + doc['c']


@logged
def do_nothing(con, my):
    return con


if __name__ == '__main__':
    """average testing"""
    for i in range(1, 4):
        print(do_nothing_avg(i))
    """log testing"""
    do_nothing1(3, {'c': 4}, con=True, my='False')
    do_nothing(con=True, my='False')
    do_nothing2()
