## Theory

Our current plot is not very informative because the data has a long right tail — a few games have extremely high sales.
This stretches the x-axis, making it hard to analyze the main distribution.

One way to address this issue is by setting an upper limit for sales. However, how can we determine a reasonable
threshold?

A good approach is to apply a logarithmic scale to the x-axis. This transformation helps spread out the lower values
while compressing the extreme ones, making the distribution clearer. With this view, we can define a meaningful sales
cutoff.

To enable this, set the `log_scale` argument to `True` in the `displot` function.

## Task

Apply a logarithmic scale to the x-axis of the histogram to  understand the upper limit of sales better.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>