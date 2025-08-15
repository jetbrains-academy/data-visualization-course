## Theory

Great! Now our histogram clearly shows the key pattern: there are far fewer games with high sales than those with low
sales. Next, let’s use histograms to compare the sales distributions of different publishers.

Matplotlib's `hist` allows plotting multiple distributions on the same figure in several ways:

1. Overlaid on the same axis with different transparency
2. Stacked on top of each other
3. Separated into subplots for each distribution
4. Grouped histograms. Unlike overlaid histograms, bins are placed next to each other rather than overlapping.

We will focus on overlaid histograms, as they are great for direct comparisons. To achieve this, we can plot histograms
one at a time by calling `hist` for each distribution.

## Task

1. Plot two overlaid histograms for the global sales distributions of games published by `Electronic Arts` and `Ubisoft`.

2. For each histogram, set `alpha` to `0.7` and use the default value for `bins`. We described the `alpha` parameter in details in
the "[Transparency and color](course://1_2_line_and_scatter_plots_matplotlib/1_theory/2_transparency_and_color)"
section. Find more details in the corresponding hint below.

3. Use the hidden `filter_by_publisher` function to filter the data for the given publisher. 
Pass the dataset and the publisher name as arguments.
Then, use the hidden `filter_by_global_sales` function to filter out global sales above the 95th percentile.

If you prefer, you can filter the dataset manually. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="How should I filter the data?">
    To filter the data by publisher, you can use boolean indexing on the <code>publisher</code> column.
</div>

<div class="hint" title="How to set transparency?">
    Specify the <code>alpha</code> parameter in the <code>hist</code> method.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
