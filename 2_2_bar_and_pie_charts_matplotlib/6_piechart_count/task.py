import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame):
    data = games[["year_of_release", "eu_sales", "jp_sales", "na_sales", "other_sales"]]
    data["year_of_release"] = data["year_of_release"].dt.year
    data = data[data.year_of_release.isin([1990.0, 2000.0, 2010.0, 2015.0])]

    data = data.melt(id_vars="year_of_release", var_name="region", value_name="sales")

    data["region"] = data["region"].str.replace("_sales", "")
    data = data.groupby(["year_of_release", "region"])["sales"].sum().reset_index()

    return sns.catplot(x="year_of_release", y="sales", hue="region", data=data, kind="bar")


def main():
    games = read()
    games = preprocess(games)

    fig = plot(games)
    fig.savefig("plot.png", dpi=300)


if __name__ == "__main__":
    main()
