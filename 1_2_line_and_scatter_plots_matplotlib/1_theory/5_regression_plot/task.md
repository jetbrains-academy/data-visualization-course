## Theory

Now we can definitely see an uptrend, but it is not a straight line.
How do we plot a straight line showing a trend?
For that, we can use the method called linear regression.
In simple words, it tries to build a line between our data points in such a way that the mean error is minimized.

The `aggregate` function now estimates the critic scores using the regression line.
If you want, you can implement it by yourself.
Please see the corresponding hint below.

Previously, we only used oe type of visualization, but what if we want to build a scatter plot along with a line?
Using matplotlib, we can easily do it,
just call another method from `Axes`, and it will be plotted on the top of the previous ones.

## Task

Add the scatter plot to the same figure.

## Hints

<div class="hint" title="How the figure should look like?">
   <img src="example.png" alt="How the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I aggregate the data?">
   To aggregate the data, we can use numpy:
   <ol>
      <li>Calculate regression line coefficients using <a href="https://numpy.org/doc/stable/reference/generated/numpy.polyfit"><code>polyfit</code></a>. The degree of the fitting polynomial should be 1.</li>
      <li>Create regression function using <a href="https://numpy.org/doc/stable/reference/generated/numpy.poly1d"><code>poly1d</code></a>. This function will accept <code>user_score</code> and return approximate <code>critic_score</code>.</li>
      <li>Create a new dataframe, where the <code>user_score</code> column should contain only unique values and the <code>critic_score</code> is a result of applying the function from the second step to the new <code>user_score</code> column.</li>
   </ol>

   If you have some difficulties with your own preprocessing, you can
   have [a sneak peek into inner file](file://1_2_line_and_scatter_plots_matplotlib/1_theory/5_regression_plot/data.py)
   where our preprocessing is defined.

   Note that your own aggregation function will not be tested.
</div>
