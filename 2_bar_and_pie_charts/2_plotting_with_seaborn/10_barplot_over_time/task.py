import pandas as pd
import seaborn as sns

from data import read, preprocess


def plot(games: pd.DataFrame):
    selected_platforms = {"PS4", "XOne", "PC", "WiiU"}
    new_games = games[games.year_of_release > pd.to_datetime("2014-01-01")]
    selected_games = new_games[new_games.platform.isin(selected_platforms)]

    count_df = selected_games.groupby(["platform", "genre"]).size().reset_index(name="count")

    # Calculate total count for each platform
    platform_total = selected_games.groupby("platform")["genre"].count().reset_index(name="total")

    # Merge the count dataframe with the total dataframe
    count_df = count_df.merge(platform_total, on="platform")

    # Calculate the proportion for each genre within each platform
    count_df["proportion"] = count_df["count"] / count_df["total"]

    # Sorting by proportions within each platform
    count_df.sort_values(by=["platform", "proportion"], ascending=[True, False], inplace=True)

    # Get the order of genres for each platform based on the proportions
    order = count_df.groupby("platform").apply(lambda x: x["genre"].tolist()).to_dict()

    # Create a categorical plot using seaborn, showing proportions
    sns.catplot(
        data=count_df,
        kind="bar",
        x="platform",
        y="proportion",
        hue="genre",
        hue_order=order[selected_games["platform"].iloc[0]],  # Use calculated order
        height=5,
        aspect=1.5,
        order=selected_games["platform"].unique(),  # Preserve order of appearance in original data
    )


def main():
    games = read()
    games = preprocess(games)

    plot(games)


if __name__ == '__main__':
    main()
