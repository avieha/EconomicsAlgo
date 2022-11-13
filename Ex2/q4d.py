"""
Using cvxpy - the convex optimization package of Python -
to find a fair and efficient division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

import cvxpy

# print("\n\n\nPROBLEM #1")
# print("Two resources (Oil, Steel) has to be divided among two people with values:")
# print("0   1")
# print("1-t  t")

t = cvxpy.Variable(pos=True)
Ami_steel = cvxpy.Variable(pos=True)
# Ami_oil = cvxpy.Variable(pos=True)
Tami_steel = cvxpy.Variable(pos=True)
Tami_oil = cvxpy.Variable(pos=True)  # fractions of the three resources given to Ami

utility_ami = Ami_steel
utility_tami = Tami_oil + Tami_steel

constraints = [0.5 <= t, t <= 1, Ami_steel == 1,
               Tami_steel + Tami_oil == 1, utility_ami <= 1, utility_tami <= 1]

prob = cvxpy.Problem(
    cvxpy.Maximize(utility_tami * utility_ami),
    constraints)
prob.solve(qcp=True)
print("status:", prob.status)
print("optimal value: ", prob.value)
print("Fractions given to Ami: ", Ami_steel.value)
print("Fractions given to Tami: ", Tami_steel.value + Tami_oil.value)
print("Utility of Ami", utility_ami.value)
print("Utility of Tami", utility_tami.value)
