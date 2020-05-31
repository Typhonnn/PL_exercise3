import inspect


def group_types(arr):
    return {'i': list(filter(lambda x: isinstance(x, int), arr)), 'c': list(filter(lambda y: isinstance(y, str), arr)),
            'f': list(filter(lambda z: isinstance(z, float), arr)), 'o': list(
            filter(lambda w: not isinstance(w, int) and not isinstance(w, str) and not isinstance(w, float), arr))}


def one_param_func(arr):
    return list(filter(lambda x: len(inspect.signature(x).parameters) <= 1, arr))


if __name__ == '__main__':
    my_list = [1, 'h', 2.5, 3, 'e', [5, 6.5], ("tuple", 1)]
    res_groups = group_types(my_list)
    print(res_groups)
    func_list = [group_types, one_param_func]
    one_param = one_param_func(func_list)
    print(one_param)
