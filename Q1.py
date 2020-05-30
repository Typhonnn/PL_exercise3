from collections import Counter


def find_dividers(num):
    arr = []
    for i in range(1, int(num / 2 + 1)):
        modulo = num % i
        if modulo == 0:
            arr.append(i)
    return sum(arr) >= num


def dividers_to_list(num):
    arr = []
    for i in range(1, int(num / 2 + 1)):
        modulo = num % i
        if modulo == 0:
            arr.append(i)
    return arr


def sum_of_dividers(numbers):
    return Counter(sorted(i for num in filter(find_dividers, numbers) for i in range(1, int(num/2) + 1) if num % i == 0))


if __name__ == '__main__':
    dividers_counter = sum_of_dividers([64, 53, 28, 34, 12])
    print(dividers_counter)
