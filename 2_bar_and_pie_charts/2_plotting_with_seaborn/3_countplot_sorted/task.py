import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame):
    sns.countplot(data=games, y="platform", order=games["platform"].value_counts().index)


def main():
    games = read()
    games = preprocess(games)

    plot(games)


if __name__ == "__main__":
    main()
