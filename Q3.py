"""Tal Balelty - 312270291"""


class AverageIO:
    """Calculates the average of all function's inputs and outputs so far."""

    def __init__(self, func):
        self.func = func
        self.counter = 0
        self.averages = ()

    def __call__(self, *args):
        ret = self.func(*args)
        if self.counter == 0:
            self.averages = (*args, ret)
            self.counter += 1
        else:
            param_avg = self.averages[0] * self.counter
            res_avg = self.averages[1] * self.counter
            self.counter += 1
            param_avg = (param_avg + args[0]) / self.counter
            res_avg = (res_avg + ret) / self.counter
            self.averages = (param_avg, res_avg)
        print("Average Results: {}".format(self.averages))
        return ret


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
                kwargs_param = str(kwargs) + ')'
            else:
                args_param = args_param[:-2] + ')'
        elif kwargs:
            kwargs_param = '({})'.format(kwargs)
        logged.messages.append("You called {}{}{} it returned {}".format(func.__name__, args_param, kwargs_param, ret))
        for msg in logged.messages:
            print(msg)
        return ret

    return run


"""Testing functions:"""


@AverageIO
@logged
def do_nothing_avg(num):
    return num + 2


@logged
def do_nothing1(num, doc, con, my):
    return num + doc['c']


@logged
def do_nothing(con, my):
    return con


if __name__ == '__main__':
    for i in range(1, 5):
        print(do_nothing_avg(i))
    do_nothing1(3, {'c': 4}, con=True, my='False')
    do_nothing(con=True, my='False')
