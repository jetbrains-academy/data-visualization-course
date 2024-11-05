## Theory

Let's try to understand what is going on in our graph. We can definitely see an uptrend, but it is not a straight line.
This occurs because `relplot` can only plot simple lines, and when it comes to data preprocessing before plotting,
it performs common aggregations like calculating the mean, median, min, max, etc.

In our case, by default, it calculated the mean of the `critic_score` values that correspond to a common `user_score`.
The aggregation function can be customized with the `estimator` parameter.
The area around the line represents an error bar, indicating how well the aggregation represents the initial data.
There are [several types of error bars](https://seaborn.pydata.org/tutorial/error_bars.html), which can be set with
the `errorbar` parameter.

We will learn more about `estimator` and `errorbar` 
in the [next Seaborn section](course://2_1_bar_and_pie_charts_seaborn/1_theory/3_countplot_stats).

So, how do we plot a straight line that shows a trend?
For that, we can use the Seaborn function [`lmplot`](https://seaborn.pydata.org/generated/seaborn.lmplot.html),
which plots the data along with a linear regression model fit.

## Task

Modify the `plot` function by replacing the `relplot` call with `lmplot` and removing the `kind` parameter.

## Hints

<div class="hint" title="How does linear regression work?">
    Linear regression finds the best-fitting straight line through the data by minimizing the difference between 
    predicted and actual values. This is done by minimizing the squared errors between the line and the data points. 
    The equation of the line is: <code>y = mx + b</code>, where <code>m</code> is the slope and <code>b</code> is the
    intercept.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
