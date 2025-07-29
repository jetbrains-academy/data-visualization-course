## Theory

Great! Now our histogram clearly shows the key pattern: there are far fewer games with high sales than those with low
sales. Next, let’s use histograms to compare the sales distributions of different publishers.

Seaborn's `displot` allows plotting multiple distributions on the same figure in several ways:

1. Overlaid on the same axis with transparency
2. Stacked on top of each other
3. Separated into subplots for each distribution

We will focus on overlaid histograms, as they are great for direct comparisons. To achieve this, we can use the `hue`
argument to split the data by a categorical column.

## Task

1. Use the hidden `filter_by_publisher` function to filter the data only for `Ubisoft` and `Electronic Arts`.
Then, use the hidden `filter_by_global_sales` function to filter out global sales above the 95th percentile.

2. Pass the `publisher` column to the `hue` argument to distinguish the distributions.

If you prefer, you can filter the dataset manually. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="How should I filter the data?">
    To filter the data by publisher, 
    you can use boolean indexing and the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin"><code>isin</code></a> method on the <code>publisher</code> column.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
