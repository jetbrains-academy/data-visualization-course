## Task

During some experiment, researchers recorded the subject's `y` variable while changing the `x` variable.
This was a secret research, so they haven't told us any additional information about it, but they said they found something unusual in the observations.
They need to find the trend in the data, so they're looking for help with plotting.
Let's help them!

Our figure should consist of two traces: line and scatter.
The line trace should plot a regression line, and the scatter trace should plot actual data.

You should also make several visual adjustments:

1. The line trace should bе of `navy` color.
2. The scatter trace should be `grey` and almost transparent (`0.05`).

Note that you don't need to make any preprocessing of the data.

If you get stuck,
please feel free to use hints bellow where you can also find what the final figure should look like.

## Further customization

If you want, you can play with the figure style further. Here are some ideas for the customization:

1. You can change the number of ticks in the figure.
2. You can plot more complex approximation of the data (using the `approximated_y` column).
3. You can add a legend and title.

We encourage you to learn how to do it yourself, because not all of these customizations will be covered in the course.

Note that these changes will not be tested and might break existing tests.

## Hints

<div class="hint" title="How the figure should look like?">
    <img src="example.png" alt="How the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="What function should we use?">
   As we need to plot both scatter and regression line, the best choice is to use <code>sns.lmplot</code>.
   
   To customize the line and scatter look inside the figure, you can use the <code>line_kws</code> and <code>scatter_kws</code> parameters.
</div>

<div class="hint" title="How to color the trace?">
    To color line or scatter, you can use the <code>color</code> argument:
    <code>sns.relplot(x="x", y="y", data=my_data, color="color_name")</code>
</div>

<div class="hint" title="How to make the trace transparent?">
    To make line or scatter transparent, you can use the <code>alpha</code> argument:
    <code>sns.relplot(x="x", y="y", data=my_data, alpha=0.5)</code>
</div>
