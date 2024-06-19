import pandas as pd
import seaborn as sns
from seaborn.relational import relplot

from data import read, preprocess


def plot(games: pd.DataFrame) -> sns.FacetGrid:
    return relplot(games, x='user_score', y='critic_score', kind='line')


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == '__main__':
    main()
