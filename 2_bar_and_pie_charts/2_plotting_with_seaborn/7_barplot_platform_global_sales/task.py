import pandas as pd
import seaborn as sns

from data import read, preprocess


def plot(games: pd.DataFrame):
    selected_platforms = {"PS4", "XOne", "PC", "WiiU"}
    new_games = games[games.year_of_release > pd.to_datetime("2014-01-01")]
    selected_games = new_games[new_games.platform.isin(selected_platforms)]

    sns.barplot(data=selected_games, x="platform", y="global_sales")


def main():
    games = read()
    games = preprocess(games)

    plot(games)


if __name__ == '__main__':
    main()
