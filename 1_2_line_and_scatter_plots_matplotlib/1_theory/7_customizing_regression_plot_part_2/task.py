import matplotlib.pyplot as plt
import pandas as pd

from data import aggregate, preprocess, read


def plot(games: pd.DataFrame) -> plt.Figure:
    aggregated_games = aggregate(games)

    fig, ax = plt.subplots()

    ax.scatter("user_score", "critic_score", data=games, alpha=0.1)
    ax.plot("user_score", "critic_score", data=aggregated_games, color="firebrick")

    ax.set_xlabel("User Score")
    ax.set_ylabel("Critic Score")

    ax.set_xticks(range(11))
    ax.set_yticks(range(0, 101, 10))

    ax.spines[["right", "top"]].set_visible(False)

    return fig


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
