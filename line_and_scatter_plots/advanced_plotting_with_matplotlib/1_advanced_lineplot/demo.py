import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator

from data import read


def plot(df: pd.DataFrame):
    x = df.x.to_numpy()
    y = df.approximated_data.to_numpy()
    y_noisy = df.experimental_data.to_numpy()

    fig, main_ax = plt.subplots(figsize=(4, 4))

    main_ax.set_xticks([-4, 0, 4])
    main_ax.set_xlim(-4, 4)

    main_ax.set_yticks([-1.5, 0, 1.5])
    main_ax.set_ylim(-2, 2)

    main_ax.spines[["right", "top"]].set_visible(False)

    inset_ax = main_ax.inset_axes(
        [0.15, 0.7, 0.3, 0.3],
        xlim=[0.5, 1.5],
        ylim=[0.6, 1.1],
        xticks=[0.5, 1.5],
        yticks=[0.6, 1.1],
    )

    line_width = 1.5
    for ax in main_ax, inset_ax:
        ax.scatter(
            x,
            y_noisy,
            edgecolor="k",
            facecolor="none",
            lw=1,
            s=5,
            zorder=1,
            alpha=0.2,
        )
        ax.plot(
            x,
            y,
            color="firebrick",
            lw=line_width,
            zorder=2,
        )

        ax.tick_params(which="minor", axis="both", length=4, width=line_width)
        ax.tick_params(which="major", axis="both", length=8, width=line_width)

        for axis in ["top", "bottom", "left", "right"]:
            ax.spines[axis].set_linewidth(line_width)

    box, pth = main_ax.indicate_inset_zoom(inset_ax, edgecolor="k", alpha=1)
    for p in [box] + list(pth):
        p.set_linestyle("dashed")
        p.set_linewidth(line_width)

    plt.show()


def main():
    experiment = read()
    plot(experiment)


if __name__ == "__main__":
    main()
