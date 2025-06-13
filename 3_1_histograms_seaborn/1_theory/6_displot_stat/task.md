## Theory

When comparing distributions with different sample sizes, using raw counts can be misleading. For example, if one publisher has released significantly more games than another, its bars will naturally be higher, even if the distributions are the same.

To address this, we can normalize histograms so they show proportions (or probabilities) instead of raw counts. This ensures that differences in sample size do not affect the histograms.

In Seaborn's `displot` function, we can achieve this by setting the `stat` parameter to one of the following:
- `count` (default) – Displays the number of observations in each bin.
- `frequency` – Similar to `count` but normalized by bin width.
- `probability` or `proportion` – Shows the proportion of observations in each bin (summing to `1`).
- `percent` – Shows the percentage of observations in each bin (summing to `100`).
- `density` – Similar to `probability`, but the total area under bars equals `1`.

## Task

Modify the histogram to show probabilities instead of counts.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
