## Task

A beverage company has been successfully operating in Belgrade, selling a variety of drinks throughout the year. Now,
they have decided to expand their business to Yerevan and want to compare their established sales in Belgrade with the
initial six months of sales in Yerevan to assess market differences and optimize its strategy.

Because the two markets differ in size, seasonality, and customer preferences, the company wants to see if Yerevan’s
sales patterns, despite the shorter observation period, resemble those in Belgrade. If both follow a similar
distribution, it might suggest that the factors influencing sales are consistent across cities. Conversely, distinct distributions could indicate unique local influences affecting sales.

To reveal these overall trends, the company has asked us to create a single plot with two overlapping histograms.

Visualization requirements:

1. The histogram should be an unfilled line plot.
2. The histogram should be normalized (the bins should sum to `1`).
3. Both histograms should have common bins, ranging from the lowest rounded-down hundred to the highest rounded-up
   hundred across both cities, with a step of `100`.
4. Yerevan's data should be colored `crimson`, and Belgrade's data should be colored `black`.
5. The x-axis label should be `'Sales'`.
6. The y-axis label should be `'Probability'`.
7. Add a title: `'Sales Distribution in Belgrade and Yerevan'`.
8. Add a legend with the city names.

Note that there is no need to preprocess the data here.

You can use the following hidden functions:

1. `get_city_sales`: Retrieves sales data for a specific city. Pass the dataset and the city name as arguments.
2. `get_weights`: Retrieves the weights for a specific city.
3. `get_bins`: Retrieves the bin edges for the plot (common for both cities). Pass the whole dataset as an argument!

If you get stuck, please feel free to use the hints below, where you can also find an example of what the final figure should look
like.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to plot two histograms on the same plot?">
    To plot two histograms on the same figure, call the <code>hist</code> method separately for each city, 
    ensuring both plots share the same <code>ax</code> object.
</div>

<div class="hint" title="How to normalize the histogram?">
   To normalize the histogram, set the <code>weights</code> parameter of the <code>hist</code> method to 
   \(\frac{1}{n}\) for each city, where <code>n</code> is the number of observations in that city.
</div>

<div class="hint" title="How to make the histogram an unfilled line plot?">
   Use <code>histtype='step'</code> in the <code>hist</code> method. This will create an outline-only version of the
   histogram, without any fill.
</div>

<div class="hint" title="How to set colors for the histogram?">
   If <code>histtype='step'</code> is used, the <code>color</code> parameter sets the line color.
</div>

<div class="hint" title="How to change the number of bins?">
   To change the number of bins, specify the <code>bins</code> parameter in the <code>hist</code> method.
</div>

<div class="hint" title="How to add axis labels?">
   You can pass the desired label to the 
   <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel">
   <code>set_xlabel</code></a> and 
   <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel">
   <code>set_ylabel</code></a> methods: <code>ax.set_xlabel('x')</code> and <code>ax.set_ylabel('y')</code>.
</div>

<div class="hint" title="How to set a title?">
    Pass the desired title of the plot to the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html">
    <code>set_title</code></a> method: <code>ax.set_title("title")</code>.
</div>

<div class="hint" title="How to add a legend?">
    First, specify the <code>label</code> parameter in the <code>hist</code> method for each city.
    Then, call the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html">
    <code>ax.legend</code></a> method.
</div>
