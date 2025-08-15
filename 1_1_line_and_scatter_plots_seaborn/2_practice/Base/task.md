## Task

During an experiment, researchers recorded the subject's `y` variable while changing the `x` variable.
This was a secretive study, so they haven't provided any additional details, but they mentioned finding something unusual in the observations.
They need to identify the trend in the data, so they're seeking help with plotting.
Let's assist them!

Our figure should consist of two traces: a line and a scatter plot.
The line trace should represent a regression line, while the scatter trace should display the actual data points.

We should also make several visual adjustments:

1. The line trace should bе `navy` blue.
2. The scatter trace should be `grey` and almost transparent (`0.05`).

Note that no data preprocessing is required.

If you get stuck,
please feel free to use the hints below, which also show what the final figure should look like.

## Further customization

If you want, you can further customize the figure. Here are some ideas for the customization:

1. You can change the number of ticks in the figure.
2. You can plot a more complex approximation of the data (using the `approximated_y` column).
3. You can add a legend and a title.

We encourage you to explore how to make these adjustments on your own, as not all of these customizations will be covered in the course.

Please note that these changes will not be tested and might break existing tests.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="What function should we use?">
   Since we need to plot both a scatter plot and a regression line, the best choice is to use <code>sns.lmplot</code>.
   
   To customize the appearance of the line and scatter plot within the figure, you can use the <code>line_kws</code> and <code>scatter_kws</code> parameters.
</div>

<div class="hint" title="How to color the trace?">
    To color the line or scatter plot, you can use the <code>color</code> argument:
    <code>sns.relplot(x="x", y="y", data=my_data, color="color_name")</code>.
</div>

<div class="hint" title="How to make the trace transparent?">
    To make the line or scatter plot transparent, you can use the <code>alpha</code> argument:
    <code>sns.relplot(x="x", y="y", data=my_data, alpha=0.5)</code>
</div>
