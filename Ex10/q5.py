import statistics
from typing import List
import doctest


def binary_search(start, end, citizen_votes, C):
    # print("citizen votes:", citizen_votes)
    while end > start:
        functions = []
        merged = []
        t = (start + end) / 2
        for i in range(1, len(citizen_votes)):
            functions.append(C * min(1, i * t))
        # print("\nt:", t, "linear functions:", functions)
        for i in range(len(citizen_votes[0])):  # iterating each topic, merging with functions
            vec = []
            for citizen in citizen_votes:
                vec.append(citizen[i])
            vec += functions
            vec.sort()
            merged.append(vec)
        medians_list = [statistics.median(vec) for vec in merged]
        medians_sum = sum(medians_list)
        if medians_sum < C:
            start = t
        if medians_sum > C:
            end = t
        if medians_sum == C:
            return t, medians_list


def compute_budget(total_budget: float, citizen_votes: List[List]) -> List[float]:
    """
    :param total_budget:
    :param citizen_votes:
    :return:
    >>> citizen_votes = [[0, 0, 6, 0, 0, 6, 6, 6, 6], [0, 6, 0, 6, 6, 6, 6, 0, 0], [6, 0, 0, 6, 6, 0, 0, 6, 6]]
    >>> compute_budget(30, citizen_votes)
    [2.0, 2.0, 2.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
    >>> citizen_votes = [[100, 0, 0], [0, 0, 100]]
    >>> compute_budget(100, citizen_votes)
    [50.0, 0, 50.0]
    >>> citizen_votes = [[100, 0, 0], [0, 0, 100], [0, 0, 100]]
    >>> compute_budget(100, citizen_votes)
    [33.333333333333336, 0, 66.66666666666667]
    >>> citizen_votes = [[100, 0, 0], [0, 0, 100], [0, 50, 50],[30,70,0]]
    >>> compute_budget(100, citizen_votes)
    [30, 35.00000000000001, 35.00000000000001]
    """
    return binary_search(0, 1, citizen_votes, total_budget)


if __name__ == '__main__':
    # failures, tests = doctest.testmod(report=True)
    # print("{} failures, {} tests".format(failures, tests))
    citizen_votes = [[100, 0, 0], [0, 0, 100], [0, 50, 50], [30, 70, 0]]
    print(compute_budget(100, citizen_votes))
