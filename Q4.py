class LastThree:
    def __init__(self, func):
        self.func_list = []
        self.current_func = func

    def __call__(self, *args):
        ret = self.current_func(*args)
        self.func_list.append(self.current_func)
        end = len(self.func_list)
        if end >= 3:
            for index in range(end - 3, end):
                print(self.func_list[index].__name__)
        return ret


@LastThree
def sum_numbers(num):
    total = num + 2
    return total


if __name__ == '__main__':
    for i in range(1, 6):
        print(sum_numbers(i))
