import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from data import preprocess, read


def plot(games: pd.DataFrame):
    needed_regions = ("eu_sales", "jp_sales")
    df_tmp = games[[col for col in games.columns if "sales" in col and col in needed_regions]]
    df_melted = df_tmp.melt(var_name="region", value_name="sales")
    df_melted["region"] = df_melted["region"].apply(lambda x: x.split("_")[0])

    # Quantile filtering
    thresholds = df_melted.groupby("region")["sales"].quantile(0.95)
    result_df = pd.DataFrame()

    for region, threshold in thresholds.items():
        filtered_df = df_melted[(df_melted["region"] == region) & (df_melted["sales"] < threshold)]
        result_df = pd.concat([result_df, filtered_df])

    sns.histplot(
        data=result_df,
        x="sales",
        hue="region",
        bins=10,
        element="step",
        stat="density",
        common_norm=False,
    )


def main():
    games = read()
    games = preprocess(games)

    plot(games)
    plt.show()


if __name__ == "__main__":
    main()
