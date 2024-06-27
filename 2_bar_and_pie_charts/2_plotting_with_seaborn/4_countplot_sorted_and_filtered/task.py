import pandas as pd
import seaborn as sns

from data import read, preprocess


def plot(games: pd.DataFrame):
    new_games = games[games.year_of_release > pd.to_datetime("2014-01-01")]
    sns.countplot(data=new_games, y="platform", order=new_games["platform"].value_counts().index)


def main():
    games = read()
    games = preprocess(games)

    plot(games)


if __name__ == '__main__':
    main()
