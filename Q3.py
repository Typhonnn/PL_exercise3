class AverageIO:
    def __init__(self, func):
        self.func = func
        self.averages = ()

    def __call__(self, *args):
        ret = self.func(*args)
        if len(self.averages) == 0:
            self.averages = (*args, ret)
        else:
            self.averages = ((self.averages[0] + args[0]) / 2, (self.averages[1] + ret) / 2)
        print("Average Results: {}".format(self.averages))
        return ret


def logged(func):
    def run(*args):
        ret = func(*args)
        print("You called {}({}) it return {}".format(func.__name__, *args, ret))
        return ret

    return run


@AverageIO
@logged
def sum_numbers(num):
    total = num + 2
    return total


if __name__ == '__main__':
    for i in range(1, 5):
        print(sum_numbers(i))
