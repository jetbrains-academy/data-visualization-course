## Theory

Our histogram now provides a clearer view of the distribution, but it may still be too detailed. Using too many bins
can cause small fluctuations in the data to create a noisy appearance, making it harder to see overall trends.

The number of bins determines the balance between detail and smoothness:

- Too many bins: Reveals fine details but introduces noise.
- Too few bins: Smooths the data but may hide important patterns.
- Just right: Preserves key trends while reducing unnecessary noise.

By default, Seaborn determines the number of bins by selecting the minimum bin width according to
the [Sturges's rule](https://en.wikipedia.org/wiki/Sturges%27s_rule)
and the [Freedman-Diaconis rule](https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule).
However, you can manually configure the bins using the `bins` argument in the `displot` function. This argument accepts:

- An integer: The number of bins to use.
- A collection: The edges of the bins (supports non-uniform widths).
- A string: The method used to calculate the number of bins. For a full list of accepted strings,
  refer to the [documentation](https://numpy.org/doc/stable/reference/generated/numpy.histogram_bin_edges.html).

## Task

Set the number of bins in the histogram to `10`.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
