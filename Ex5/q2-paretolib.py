from paretoset import paretoset
import pandas as pd
import matplotlib.pyplot as plt

salespeople = pd.DataFrame(
    {
        "value": [20, 10, 30, 40, 40, 20, 30, 10],
        "partition": [0.1, 0.3, 0.6, 1, 0.9, 0.7, 0.7, 0],
    }
)
mask = paretoset(salespeople, sense=["max", "max"])
top_performers = salespeople[mask]
plt.plot(salespeople["value"], salespeople["partition"], 'bo')
plt.plot(top_performers["value"], top_performers["partition"], 'ro')
# plt.plot(without_points, 'blue')
# plt.title("Comparison With vs Without pruning")
plt.xlabel("value")
plt.ylabel("partition")
plt.grid()
plt.show()
