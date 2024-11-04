import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame):
    df_selected_eu = games[games.eu_sales <= games.eu_sales.quantile(0.95)]
    sns.histplot(data=df_selected_eu, x="eu_sales", bins=20, stat="probability")

    df_selected_jp = games[games.jp_sales <= games.jp_sales.quantile(0.95)]
    sns.histplot(data=df_selected_jp, x="jp_sales", bins=20, stat="probability")


def main():
    games = read()
    games = preprocess(games)

    plot(games)
    plt.show()


if __name__ == "__main__":
    main()
