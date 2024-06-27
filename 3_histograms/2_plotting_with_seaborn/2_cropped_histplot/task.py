import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from data import read, preprocess


def plot(games: pd.DataFrame):
    df_selected = games[games.global_sales <= games.global_sales.quantile(0.95)]
    sns.histplot(data=df_selected, x="global_sales")


def main():
    games = read()
    games = preprocess(games)

    plot(games)
    plt.show()


if __name__ == "__main__":
    main()
