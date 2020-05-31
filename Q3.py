class AverageIO:
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
    logged.messages = []

    def run(*args, **kwargs):
        ret = func(*args, **kwargs)
        param = ''
        for a in args:
            param += "{},".format(a)
        for k in kwargs.items():
            param += "{},".format(k)
        param = "({})".format(param)
        logged.messages.append("You called {}{} it returned {}".format(func.__name__, param, ret))
        for msg in logged.messages:
            print(msg)
        return ret

    return run


@AverageIO
@logged
def sum_numbers(num):
    return num + 2


@logged
def sum_numbers1(num, doc, con):
    return num + doc['c']


if __name__ == '__main__':
    for i in range(1, 5):
        print(sum_numbers(i))
    sum_numbers1(3, {'c': 4}, con=True)
