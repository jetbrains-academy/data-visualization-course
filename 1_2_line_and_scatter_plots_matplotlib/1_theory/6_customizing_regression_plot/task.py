import pandas as pd
import matplotlib.pyplot as plt

from data import preprocess, read, aggregate


def plot(games: pd.DataFrame) -> plt.Figure:
    aggregated_games = aggregate(games)

    fig, ax = plt.subplots()

    ax.scatter('user_score', 'critic_score', data=games, alpha=0.1)
    ax.plot('user_score', 'critic_score', data=aggregated_games, color='firebrick')

    return fig


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
