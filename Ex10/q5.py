import statistics
from typing import List


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
        # print("merged:", merged)
        medians_list = find_median(merged)
        medians_sum = sum(medians_list)
        if medians_sum < C:
            start = t
        if medians_sum > C:
            end = t
        if medians_sum == C:
            return t, medians_list


def find_median(merged):
    medians = []
    for vec in merged:  # iterating each topic
        medians.append(statistics.median(vec))
    return medians


def compute_budget(total_budget: float, citizen_votes: List[List]) -> List[float]:
    print(binary_search(0, 1, citizen_votes, total_budget))


if __name__ == '__main__':
    citizen_votes = [[100, 0, 0], [0, 0, 100]]
    compute_budget(100, citizen_votes)
