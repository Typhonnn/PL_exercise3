def last_three(func):
    """prints the last 3 functions that were called."""
    last_three.func_list = []

    def run(*args):
        ret = func(*args)
        last_three.func_list.append(func)
        end = len(last_three.func_list)
        if end >= 3:
            for index in range(end - 3, end):
                print(last_three.func_list[index].__name__)
        return ret
    return run


@last_three
def sum_numbers(num):
    total = num + 2
    return total


if __name__ == '__main__':
    for i in range(1, 6):
        print(sum_numbers(i))
