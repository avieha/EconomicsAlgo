import doctest

import cvxpy


def ordered_partition(value_vec, partition_vec):
    """
        checks if the partition is ordered, if it does return True
        else, returns Pareto improve of the partition

        :param value_vec: values of each item according to player.
        :param partition_vec: the partitioning as given.
        :return: True or new Pareto improve partitioning.

        >>> values = [[10, 20, 30, 40], [11, 21, 31, 41]]
        >>> partition = [[0.7, 0.4, 0, 1], [0.3, 0.6, 1, 0]]
        >>> ordered_partition(values, partition)

        >>> values = [[11, 21, 31, 41], [10, 20, 30, 40]]
        >>> partition = [[0.7, 0.4, 0, 1], [0.3, 0.6, 1, 0]]
        >>> ordered_partition(values, partition)
        True
        >>> values = [[10, 20, 30, 40], [10, 20, 30, 40]]
        >>> partition = [[0.7, 0.4, 0, 1], [0.3, 0.6, 1, 0]]
        >>> ordered_partition(values, partition)
        True
        >>> values = [[10, 20, 30, 40], [40, 30, 20, 10]]
        >>> partition = [[0.7, 0.4, 0, 1], [0.3, 0.6, 1, 0]]
        >>> ordered_partition(values, partition)
        New Partition: [['0.00', '0.00', '1.00', '1.00'], ['1.00', '1.00', '0.00', '0.00']]
        First player:
        original sum: 55.0 new: 70.00
        Second player:
        original sum: 50.0 new: 70.00
        >>> values = [[40, 10, 30, 20], [15, 20, 30, 35]]
        >>> partition = [[0, 0.4, 0.5, 1], [1, 0.6, 0.5, 0]]
        >>> ordered_partition(values, partition)
        New Partition: [['1.00', '0.00', '0.50', '0.00'], ['0.00', '1.00', '0.50', '1.00']]
        First player:
        original sum: 39.0 new: 55.00
        Second player:
        original sum: 42.0 new: 70.00
        """
    if check_ordered(value_vec, partition_vec):
        print("True")
        return

    x1, x2, x3, x4 = cvxpy.Variable(4)
    y1, y2, y3, y4 = cvxpy.Variable(4)

    part_first = x1 * value_vec[0][0] + x2 * value_vec[0][1] + x3 * value_vec[0][2] + x4 * value_vec[0][3]
    part_second = y1 * value_vec[1][0] + y2 * value_vec[1][1] + y3 * value_vec[1][2] + y4 * value_vec[1][3]

    constraints = [0 <= x1, x1 <= 1, 0 <= x2, x2 <= 1, 0 <= x3, x3 <= 1, 0 <= x4, x4 <= 1, x1 + y1 == 1, x2 + y2 == 1,
                   x3 + y3 == 1, x4 + y4 == 1]

    prob = cvxpy.Problem(
        cvxpy.Maximize(part_first + part_second), constraints)
    prob.solve()

    new_results = [["%.2f" % x1.value, "%.2f" % x2.value, "%.2f" % x3.value, "%.2f" % x4.value],
                   ["%.2f" % y1.value, "%.2f" % y2.value, "%.2f" % y3.value, "%.2f" % y4.value]]
    orig_first = orig_second = 0
    for j in range(len(partition_vec[0])):
        orig_first += partition_vec[0][j] * value_vec[0][j]
        orig_second += partition_vec[1][j] * value_vec[1][j]
    if part_first.value >= orig_first and part_second.value >= orig_second:
        print("New Partition:", new_results)
        print("First player:\noriginal sum:", orig_first, "new:", "%.2f" % part_first.value)
        print("Second player:\noriginal sum:", orig_second, "new:", "%.2f" % part_second.value)


def check_ordered(value_vec, partition_vec):
    for i in range(len(value_vec[0])):
        if partition_vec[0][i] != 0:
            ratio_first = value_vec[0][i] / value_vec[1][i]
        else:
            continue
        if partition_vec[1][i] != 0:
            ratio_second = value_vec[1][i] / value_vec[0][i]
        else:
            continue
        if ratio_second > ratio_first:
            return False
    return True


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
