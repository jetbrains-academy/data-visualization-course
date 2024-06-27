import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame):
    df_selected = games[games.global_sales <= games.global_sales.quantile(0.95)]
    sns.histplot(data=df_selected, x="global_sales", bins=10)


def main():
    games = read()
    games = preprocess(games)

    plot(games)
    plt.show()


if __name__ == "__main__":
    main()
