import matplotlib.pyplot as plt
import pandas as pd

from data import filter_by_publisher, filter_by_global_sales, preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots()

    for publisher in ["Electronic Arts", "Ubisoft"]:
        filtered_games = filter_by_publisher(games, publisher)
        filtered_games = filter_by_global_sales(filtered_games)
        ax.hist(data=filtered_games, x="global_sales", alpha=0.7)

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
