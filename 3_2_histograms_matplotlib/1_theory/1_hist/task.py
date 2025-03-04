import matplotlib.pyplot as plt
import pandas as pd

from data import preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.hist(data=games, x="global_sales")

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
