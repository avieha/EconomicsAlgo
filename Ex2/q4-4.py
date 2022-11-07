#!python3

"""
Using cvxpy - the convex optimization package of Python -
to find a fair and efficient division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy

print("\n\n\nPROBLEM #1")
print("Two resources (Oil, Steel) has to be divided among two people with values:")
print("0   1")
print("1-t  t")

t, Ami_steel, Ami_oil, Tami_steel, Tami_oil = cvxpy.Variable(5)  # fractions of the three resources given to Ami

utility_ami = Ami_steel
utility_tami = Tami_steel * t + Tami_oil * (1 - t)

print("\nEgalitarian division")

# constraints = [Tami_oil == (1 - Tami_steel), Ami_steel + Ami_oil == 1,
#                Tami_steel + Tami_oil == 1]

min_utility = cvxpy.Variable()
obj = cvxpy.Maximize(min_utility)
prob = cvxpy.Problem(
    obj,
    constraints=[0 <= Ami_steel, Ami_steel <= 1, 0 <= Tami_steel, Tami_steel <= 1, 0 <= Ami_oil, Ami_oil <= 1, 0 <= Tami_oil, Tami_oil <= 1,
                 min_utility <= utility_ami, min_utility <= utility_tami, 0 <= t, t <= 1])
prob.solve()
print("status:", prob.status)
print("optimal value: ", prob.value)
print("Fractions given to Ami: ", Ami_steel.value, Ami_oil.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)
