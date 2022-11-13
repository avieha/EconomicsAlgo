"""
Apportionment method
Also Taken from: https://github.com/martinlackner/apportionment
"""

import numpy as np
import string


def compute(
        y,
        votes,
        seats,
        parties=string.ascii_letters,
):
    return divisor(y, votes, seats, parties)


# Divisor methods
def divisor(
        y,
        votes,
        seats,
        parties=string.ascii_letters,
):
    votes = np.array(votes)
    representatives = np.zeros(len(votes), dtype=int)
    divisors = np.arange(seats) + y
    # assigning representatives
    if seats > np.sum(representatives):
        weights = np.array([p / divisors for p in votes])
        flatweights = np.sort(weights, axis=None)
        minweight = flatweights[-seats + np.sum(representatives)]
        representatives += np.count_nonzero(weights > minweight, axis=1)

    ties = False
    # dealing with ties
    if seats > np.sum(representatives):
        tiebreaking_message = (
                "  tiebreaking in order of: "
                + str(parties[: len(votes)])
                + "\n  ties broken in favor of: "
        )
        for i in range(len(votes)):
            if np.sum(representatives) == seats and minweight in weights[i]:
                if not ties:
                    tiebreaking_message = tiebreaking_message[:-2]
                    tiebreaking_message += "\n  to the disadvantage of: "
                    ties = True
                tiebreaking_message += parties[i] + ", "
            if np.sum(representatives) < seats and minweight in weights[i]:
                tiebreaking_message += parties[i] + ", "
                representatives[i] += 1
        if ties:
            print(tiebreaking_message[:-2])
    return representatives.tolist()


if __name__ == '__main__':
    parties = ['Likud', 'Yesh Atid', 'Tzionut Datit', 'Machane Mamlachti', 'Shas', 'Yahadut HaTorah', 'Yisrael Beytenu',
               'Raam',
               'Hadash-Taal', 'HaAvoda']
    votes = [1115336, 847435, 516470, 432482, 392964, 280194, 213687, 194047, 178735, 175992]
    real_results = [32, 24, 14, 12, 11, 7, 6, 5, 5, 4]
    seats = 120
    results = compute(0.999, votes, seats, parties)
    for i in range(len(results)):
        if results[i] != real_results[i]:
            print(parties[i], results[i], real_results[i])
