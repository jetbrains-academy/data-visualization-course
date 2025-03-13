## Task

A beverage company operates in both Belgrade and Yerevan, selling a variety of drinks throughout the year. To optimize
their sales strategy, they regularly analyze sales trends in different markets. Recently, they gathered sales data for a
full year in Belgrade and six months in Yerevan and want to compare how sales are distributed across these cities.

Because the two markets differ in size, seasonality, and customer preferences, the company wants to see if Yerevan’s
sales patterns, despite the shorter observation period, resemble those in Belgrade. If both follow a similar
distribution, it might suggest that the factors influencing sales are consistent across cities. If not, there could be
unique local influences at play.

To reveal these overall trends, the company asked us to create a single plot with two overlapping histograms.

Visualization requirements:

1. The histogram should be normalized (each city bins should sum to `1`).
2. Both histograms should have common bins, ranging from the lowest rounded-down hundred to the highest rounded-up
   hundred across both cities, with a step of `100`.

Note that there is no need to preprocess the data here.

You can use the hidden `get_bins` function to retrieve the bin edges for the plot (the same for both cities). Pass the
whole dataset as an argument.

If you get stuck, please feel free to use the hints below, where you can also find what the final figure should look
like.

## Further customization

If you want, you can further customize the figure. Here are some ideas for the customization:

1. Change bar color palette.
2. Add a clear figure title and axis labels.
3. Combine the histograms with other plot types.

We encourage you to explore these customizations on your own, as not all of them will be covered in this course.

Note that these changes will not be tested and might break existing tests.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to plot two histograms on the same plot?">
    To plot two histograms on the same figure, you can call the <code>displot</code> function and specify the
    <code>hue</code> parameter in it.
</div>

<div class="hint" title="How to normalize the histogram?">
    To normalize the histogram, you can set the <code>stat</code> parameter of the <code>displot</code> function to 
    <code>'probability'</code> and set the <code>common_norm</code> parameter to <code>False</code>, so that each 
    histogram is normalized separately.
</div>

<div class="hint" title="How to change the number of bins?">
    To change the default number of bins, you can specify <code>bins</code> parameter of the <code>displot</code> 
    function.
</div>

<div class="hint" title="How to generate required bin edges?">
    First, extract the minimum and the maximum value along the <code>sales</code> column in the dataset, using
    <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min"><code>min</code></a>
    and 
    <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max"><code>max</code></a>
    functions, respectively. Then,
    round the minimum down and the maximum up to the nearest hundred. Finally, generate an array of bin edges with a 
    step size of <code>100</code>, using, for example, the built-in <code>range</code> function ensuring evenly spaced 
    intervals.
</div>
