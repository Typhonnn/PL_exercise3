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
            param_avg = self.averages[0]*self.counter
            res_avg = self.averages[1]*self.counter
            self.counter += 1
            param_avg = (param_avg + args[0]) / self.counter
            res_avg = (res_avg + ret) / self.counter
            self.averages = (param_avg, res_avg)
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
