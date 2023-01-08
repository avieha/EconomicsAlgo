import copy
import doctest
import itertools


def egalitarian(items):
    """ O(n!)
    :return:
    >>> items = {'1': [40]}
    >>> egalitarian(items)
    Egalitarian partitioning: [40]
    >>> items = {'1': [40, 10], '2': [20, 33]}
    >>> egalitarian(items)
    Egalitarian partitioning: [40, 33]
    >>> items = {'1': [40, 10, 30], '2': [15, 20, 33], '3': [32, 19, 28]}
    >>> egalitarian(items)
    Egalitarian partitioning: [40, 20, 28]
    >>> items = {'1': [30,10,40], '2': [28,19,20], '3': [33,19,12]}
    >>> egalitarian(items)
    Egalitarian partitioning: [30, 19, 20]
    >>> items = {'1': [40, 10, 30, 31], '2': [15, 20, 33, 19], '3': [32, 19, 28, 20], '4': [32, 16, 28, 27]}
    >>> egalitarian(items)
    Egalitarian partitioning: [40, 20, 28, 27]
    """
    n = len(items.keys())
    lst = []
    permutations = itertools.permutations(list(items.keys()))
    for index, p in enumerate(permutations):
        temp_list = []
        for i in range(n):
            temp_list.append(items[p[i]][i])
        lst.append(temp_list)
    max_partition = []
    for part in lst:
        if not max_partition:
            max_partition = part
        if min(part) > min(max_partition):
            max_partition = part
    print("Egalitarian partitioning:", max_partition)


def leximin_egalitarian(items):
    """
    >>> items = {'1': [40]}
    >>> leximin_egalitarian(items)
    Leximin partitioning: [40]
    >>> items = {'1': [40, 10], '2': [20, 33]}
    >>> leximin_egalitarian(items)
    Leximin partitioning: [40, 33]
    >>> items = {'1': [40, 10, 30], '2': [15, 20, 33], '3': [32, 19, 28]}
    >>> leximin_egalitarian(items)
    Leximin partitioning: [32, 20, 30]
    >>> items = {'1': [30,10,40], '2': [33,19,12], '3': [28,19,20]}
    >>> leximin_egalitarian(items)
    Leximin partitioning: [33, 19, 40]
    >>> items = {'1': [40, 10, 30, 31], '2': [15, 20, 33, 19], '3': [32, 19, 28, 20], '4': [32, 16, 28, 27]}
    >>> leximin_egalitarian(items)
    Leximin partitioning: [32, 20, 28, 31]
    """
    n = len(items.keys())
    lst = []
    permutations = itertools.permutations(list(items.keys()))
    for index, p in enumerate(permutations):
        temp_list = []
        for i in range(n):
            temp_list.append(items[p[i]][i])
        lst.append(temp_list)
    max_partition = []
    for part in lst:
        if not max_partition:
            max_partition = part
        sorted_partition = sorted(part)
        sorted_max = sorted(max_partition)
        for i in range(n):
            if sorted_partition[i] >= sorted_max[i]:
                copy_max = copy.deepcopy(max_partition)
                max_partition = part
            else:
                max_partition = copy_max
                break
    print("Leximin partitioning:", max_partition)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
