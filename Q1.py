"""Tal Balelty - 312270291"""
from collections import Counter
from sympy import isprime


def find_dividers(num):
    """return True if the sum of dividers is bigger or equal to the number."""
    arr = []
    for i in range(1, int(num / 2 + 1)):
        modulo = num % i
        if modulo == 0:
            arr.append(i)
    return sum(arr) >= num


def count_dividers(numbers):
    """return dictionary of dividers and the times they appear."""
    return dict(Counter(
        sorted(i for num in filter(find_dividers, numbers) for i in range(1, int(num / 2) + 1) if num % i == 0)))


if __name__ == '__main__':
    dividers_counter = count_dividers([64, 53, 28, 34, 12])
    print(dividers_counter)
    gen_num = 5
    gen = ([False] if isprime(gen_num) else (div for div in range(1, int(gen_num / 2) + 1) if gen_num % div == 0))
    for num1 in gen:
        print(num1)
