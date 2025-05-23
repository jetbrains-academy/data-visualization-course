from matplotlib import pyplot as plt
import pandas as pd

from data import get_logarithmic_bins, preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()

    ax.hist(data=games, x="global_sales", bins=get_logarithmic_bins(games, 50))

    ax.set_xscale("log")

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
