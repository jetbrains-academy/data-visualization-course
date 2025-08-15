## Theory

Our current plot is not very informative because most of the data falls into the first two bins. The remaining bins are
barely visible due to scaling! A few games in the dataset have extremely high sales, stretching the x-axis and
making it difficult to analyze the rest of the data.

One way to address this issue is by setting an upper limit for sales. However, how can we determine a reasonable
threshold?

A good approach is to apply a logarithmic scale to the x-axis. This transformation spreads out the lower values
while compressing the extreme ones, making the distribution clearer. With this view, we can define a meaningful sales
cutoff.

The `hist` method does not allow us to set a logarithmic scale for the x-axis directly. Instead, we can apply logarithmic scaling to
the axis by calling the
[`ax.set_xscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xscale.html#matplotlib.axes.Axes.set_xscale)
method with the `log` argument.

## Task

Apply logarithmic scaling to the x-axis of the histogram to better understand the upper limit of sales.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
