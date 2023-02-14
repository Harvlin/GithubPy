import pandas as pd
import matplotlib.pyplot as plt
import sys
def plot():
    x = pd.read_csv("data4.csv")
    x.drop_duplicates(inplace=True)
    x1 = x["Duration"].mode()[0]
    x.fillna(x1, inplace=True)
    x2 = x["Calories"].mode()[0]
    x.fillna(x2, inplace=True)
    for i in x.index:
        if x.loc[i, "Duration"] > 50:
            x.drop(i, inplace=True)
    plt.plot(x["Duration"], color="r", marker="p", mec="b", label='Duration')
    plt.plot(x["Pulse"], color="g", marker="o", mec="m", label='Pulse')
    plt.plot(x["Maxpulse"], color="b", marker="o", mec="r", label='Maxpulse')
    plt.plot(x["Calories"], color="k", marker="p", mec="w", label='Calories')
    plt.title("Data", fontsize=30, loc="center")
    plt.xlabel("x-line", fontsize=17, color="black")
    plt.ylabel("y-line", fontsize=17, color="grey")
    plt.legend()
    plt.show()
    plt.savefig(sys.stdout.buffer())
    sys.stdout.flush()
plot()