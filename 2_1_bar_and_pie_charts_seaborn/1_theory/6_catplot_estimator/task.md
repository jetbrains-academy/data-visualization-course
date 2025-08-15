## Theory

Now we can see global sales per platform, but each bar has a strange line called an *error bar*.

For each platform, we have multiple global sales data points. 
Seaborn aggregates these values to plot a single value for each platform 
and provides a visual cue indicating how well this value represents the underlying data points. 

We encountered something similar when we analyzed trends using a line plot in one of the 
[previous](course://1_1_line_and_scatter_plots_seaborn/1_theory/4_lmplot) Seaborn lessons.
Now, it's time to take a closer look at the `estimator` argument.

The `estimator` argument controls how the data is aggregated. It accepts the following:
1. A callable function that maps a vector to scalar data.
2. Numpy function names like `min`, `max`, `sum`, `mean`, or `median`.

By default, Seaborn uses `mean` as the estimator.

There are [several types of error bars](https://seaborn.pydata.org/tutorial/error_bars.html),
which can be set with the `errorbar` parameter.
To disable error bars entirely, we just need to pass `None` as the value.

## Task

1. Set the estimator to `median` and remove the error bar.
2. Sort the platforms using the hidden `get_sorted_platforms` function.

   If you prefer, you can sort the platforms manually. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I sort the platforms?">
    To sort the platforms, you need to:
    <ol>
        <li>Group the data by the <code>platform</code> column using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html"><code>groupby</code></a> method.</li>
        <li>Calculate the median of the <code>global_sales</code> column using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html"><code>median</code></a> method.</li>
        <li>Sort the values using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html"><code>sort_values</code></a> method.</li>
        <li>Use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html"><code>index</code></a> property to receive sorted platform names.</li>
        <li>Convert the <code>Index</code> object to a list using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html"><code>to_list</code></a> method.</li>
    </ol>
</div>
