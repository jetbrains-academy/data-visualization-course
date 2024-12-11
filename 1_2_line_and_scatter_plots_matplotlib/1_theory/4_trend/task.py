import matplotlib.pyplot as plt
import pandas as pd

from data import aggregate, preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    aggregated_games = aggregate(games)

    fig, ax = plt.subplots()
    ax.plot("user_score", "critic_score", data=aggregated_games)

    return fig


# Please solve the task in the plot function and do not modify this one
def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
