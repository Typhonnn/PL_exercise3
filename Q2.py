"""Tal Balelty - 312270291"""
from inspect import signature


def group_types(args):
    """Groups the list of arguments in a dictionary by type."""
    return {'i': list(filter(lambda x: isinstance(x, int), args)),
            'c': list(filter(lambda y: isinstance(y, str), args)),
            'f': list(filter(lambda z: isinstance(z, float), args)), 'o': list(
            filter(lambda w: not isinstance(w, int) and not isinstance(w, str) and not isinstance(w, float), args))}


def one_param_func(funcs):
    """return a list of functions that take 1 or less arguments"""
    return list(filter(lambda x: len(signature(x).parameters) <= 1, funcs))


if __name__ == '__main__':
    my_list = [1, 'h', 2.5, 3, 'e', [5, 6.5], ("tuple", 1)]
    res_groups = group_types(my_list)
    print(res_groups)
    func_list = [group_types, one_param_func]
    one_param = one_param_func(func_list)
    print(one_param)
