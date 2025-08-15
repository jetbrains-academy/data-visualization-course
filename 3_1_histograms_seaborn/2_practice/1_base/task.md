## Task

A beverage company has been successfully operating in Belgrade, selling a variety of drinks throughout the year. Now,
the company has decided to expand its business to Yerevan and want to compare its established sales in Belgrade with the
initial six months of sales in Yerevan to assess market differences and optimize its strategy.

Because the two markets differ in size, seasonality, and customer preferences, the company wants to see if Yerevan’s
sales patterns, despite the shorter observation period, resemble those in Belgrade. If both follow a similar
distribution, it might suggest that the factors influencing sales are consistent across cities. Conversely, distinct distributions could indicate
unique local influences affecting sales.

To reveal these broader trends, the company has asked us to create a single plot with two overlapping histograms.

Visualization requirements:

1. The histogram should be normalized (i.e., the bins for each city should sum to `1`).
2. Both histograms should share common bins. These bins should range from the lowest rounded-down hundred to the highest rounded-up
   hundred across both cities, with a step of `100`.

Note that there is no need to preprocess the data here.

You can use the hidden `get_bins` function to retrieve the bin edges for the plot (the same for both cities). Pass the
entire dataset as an argument.

If you get stuck, feel free to use the hints below, where you can also find a preview of the final figure.

## Further customization

If you want, you can customize the figure even further. Here are some ideas for customization:

1. Change the color palette of the bars.
2. Add a descriptive figure title and clear axis labels.
3. Add individual observations using a scatter plot.

We encourage you to explore these customizations on your own, as not all of them will be covered in this course.

Note that these modifications will not be tested and may potentially break existing tests.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to plot two histograms on the same plot?">
    To plot two histograms on the same figure, use the <code>displot</code> function and specify the
    <code>hue</code> parameter.
</div>

<div class="hint" title="How to normalize the histogram?">
    To normalize the histogram, set the <code>stat</code> parameter of the <code>displot</code> function to 
    <code>probability</code>. Additionally, set the <code>common_norm</code> parameter to <code>False</code> to ensure that each 
    histogram is normalized separately.
</div>

<div class="hint" title="How to change the number of bins?">
    To change the default number of bins, set the <code>bins</code> parameter in the <code>displot</code> 
    function.
</div>

<div class="hint" title="How to generate the required bin edges?">
    First, extract the minimum and maximum values in the <code>sales</code> column of the dataset, using the
    <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min"><code>min</code></a>
    and 
    <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max"><code>max</code></a>
    methods, respectively. Then,
    round the minimum value down and the maximum value up to the nearest hundred. Finally, generate an array of bin edges with a 
    step size of <code>100</code>, for example, by using the built-in <code>range</code> function to ensure evenly spaced 
    intervals.
</div>
