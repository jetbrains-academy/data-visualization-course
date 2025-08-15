## Theory

Our histogram now looks better, but there are still some refinements we can make.

1. Ensure equal bins for both distributions – This allows for a more accurate comparison.
2. Improve visual clarity by adjusting the `histtype` parameter in the `hist` method.
3. Add axis labels, a legend, and a title to the plot.

By default, `histtype` is set to `bar`, which fills the bars with color. However, we can change it to `step`, which
draws a line connecting the tops of the bars without filling the area. This creates a cleaner and more
visually appealing distribution.

## Task

Modify the histogram as follows:

1. Set `histtype` to `step` to create an unfilled, line-based histogram.
2. Generate the same bin collection for both distributions. There should be `10` uniform bins, starting from the minimum
global sales value (across both publishers) and ending at the maximum value.
3. Name the x-axis as `Global Sales (millions)` and the y-axis as `Proportion`.
4. Add a title to the plot: `Global Sales Distribution for Electronic Arts and Ubisoft`.
5. Add a legend to the plot, with labels corresponding to the publishers.

You can add legend for a histogram in the same way as for a bar chart. We described it in detail in
the "[Legend](course://2_2_bar_and_pie_charts_matplotlib/1_theory/10_grouped_bar_chart_legend)" section. See the corresponding hint below for more information.

Use the hidden `get_bins` function to generate the bin collection. Pass the unfiltered dataset as an argument! 
If you prefer, you can find these values manually. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="How to add a legend with labels to the plot?">
    First, pass the <code>label</code> parameter to the <code>hist</code> method for each dataset. 
    Then, call the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html"><code>ax.legend()</code></a> method to display the legend.
</div>

<div class="hint" title="How can I generate the bins collection for both distributions?">
    Extract the minimum and maximum values from the <code>global_sales</code> column of the filtered dataset using the 
    <a href="https://numpy.org/doc/stable/reference/generated/numpy.min.html#numpy.min"><code>min</code></a> and 
    <a href="https://numpy.org/doc/stable/reference/generated/numpy.max.html#numpy.max"><code>max</code></a> functions.
    Remember, you need to find these values across both publishers.
    Then, use the <a href="https://numpy.org/doc/stable/reference/generated/numpy.linspace.html">
    <code>np.linspace</code></a> function to generate a collection of <code>10</code> uniform bins. Similar to
    <code>np.logspace</code>, it accepts 3 main parameters: <code>start</code>, <code>stop</code>, and <code>num</code>.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
