## Theory

When comparing distributions with different sample sizes, using raw counts can be misleading. For example, if one
publisher has released significantly more games than another, its bars will naturally be higher even if the
distributions are the same.

To address this, we can normalize histograms so they show proportions (or probabilities) instead of raw counts. This
ensures that differences in sample size do not affect the histograms.

In Matplotlib's `hist` method, we can achieve this by setting the `weights` parameter, which accepts a collection of values.
This parameter
specifies the weight assigned to each data point:

- By default, each data point has a weight of `1`, meaning the height of each bin represents the count of values
  within it.
- If `weights` is provided, then the height of each bin is determined by the sum of the assigned weights for all data points
  within that bin.

To normalize the histogram so that the total sum of bin heights equals `1`, we should set `weights` as $\frac{1}{n}$,
where `n` is the total number of data points.

## Task

Modify your previous histogram to show probabilities instead of counts. Keep all other parameters the same.

Use the hidden `get_weights` function to calculate the weights for a dataset filtered by publisher and global sales. If
you want to calculate the weights manually, refer to the corresponding hint below.

## Hints

<div class="hint" title="How to calculate the weights?">
    One way to do it is to use the <a href="https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html">
    <code>ones_like</code></a> function to generate an array of ones with the same shape as the data. Then, divide this
    array by the total number of data points.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
