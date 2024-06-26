import pandas as pd
import seaborn as sns

from data import read, preprocess


def plot(games: pd.DataFrame):
    sns.countplot(
        data=games,
        y="platform",
    )


def main():
    games = read()
    games = preprocess(games)

    plot(games)


if __name__ == '__main__':
    main()
