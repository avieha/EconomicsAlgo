import apportionment.methods as app
from voting import apportionment

# I've used this repo for calculating webster easily: https://github.com/martinlackner/apportionment

parties = ['Likud', 'Yesh Atid', 'Tzionut Datit', 'Machane Mamlachti', 'Shas', 'Yahadut HaTorah', 'Yisrael Beytenu',
           'Raam',
           'Hadash-Taal', 'HaAvoda']
votes = [1115336, 847435, 516470, 432482, 392964, 280194, 213687, 194047, 178735, 175992]
real_results = [32, 24, 14, 12, 11, 7, 6, 5, 5, 4]
seats = 120
webster_results = app.compute("webster", votes, seats, parties)
# webster_results = apportionment.webster(votes, seats)
same = more = less = 0
for i in range(len(webster_results)):
    if webster_results[i] < real_results[i]:
        print(parties[i], "got LESS seats using Webster", webster_results[i], "compares to: ", real_results[i])
        less += 1
    if webster_results[i] > real_results[i]:
        print(parties[i], "got MORE seats using Webster", webster_results[i], "compares to: ", real_results[i])
        more += 1
    if webster_results[i] == real_results[i]:
        print(parties[i], "got SAME seats using Webster", webster_results[i], "compares to: ", real_results[i])
        same += 1
print("\nsame:", same, "more:", more, "less:", less)
