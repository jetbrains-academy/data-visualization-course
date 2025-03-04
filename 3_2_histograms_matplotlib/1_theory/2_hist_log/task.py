from matplotlib import pyplot as plt
import pandas as pd

from data import preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.hist(data=games, x="global_sales")

    ax.set_xscale("log")
    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("example.png", dpi=300)


if __name__ == "__main__":
    main()
