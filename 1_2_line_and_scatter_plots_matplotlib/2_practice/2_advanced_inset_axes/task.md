## Task

As we can see in the figure, we have a small spike in our data.
The researchers asked us to plot it closely on the same figure, so let's try to do it.

To plot this, we can use _inset axes_. Please try to figure out on your own how to do it using
the [documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.inset_axes.html) page.

You can place the axes whether you want and make it any size.
For example, you can place it on the following coordinates: `(0.15, 0.7)` and with the following size: `(0.3, 0.3)`.

The inset axes should plot only the area of the parent axes from `x = 0.5` to `x = 1.5`, and from `y = 0.6`
to `y = 1.1`. The ticks should only mark boundaries.

After that, we can also connect our new axes with the area on the parent axes using
the [`indicate_inset_zoom`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.indicate_inset_zoom.html)
method.

If you get stuck,
please feel free to use hints bellow where you can also find what the final figure should look like.

## Further customization

If you want, you can play with the figure style further. Here are some ideas for the customization:

1. You can change the inset zoom color and style.
2. You can make all lines in the figure to have the same thickness.
3. You can add a legend and title.

We encourage you to learn how to do it yourself, because not all of these customizations will be covered in the course.

Note that these changes will not be tested and might break existing tests.

## Hints

<div class="hint" title="How the figure should look like?">
    <img src="example.png" alt="How the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to add the inset axes?">
    To add inset axes, you can use the <code>inset_axes</code> method of the <code>Axes</code> object:
    <code>ax.inset_axes([0.1, 0.5, 0.4, 0.4])</code>
</div>

<div class="hint" title="How to plot the data on the inset axis?">
    To plot the data on the inset axis, you can use the same methods and parameters as for plotting on a regular axes because it is the same <code>Axes</code> object:
    <code>inset_ax.scatter("x", "y", data=my_data, color="color_name", alpha=0.5)</code>
</div>

<div class="hint" title="How to limit the inset axes area?">
    To limit the inset axes area, you can use the <code>set_xlim</code> or <code>set_ylim</code> method of the <code>Axes</code> object:
    <code>inset_ax.set_xlim(1, 3)</code>.<br><br>
    You can also set these boundries by passing the <code>xlim</code> or <code>ylim</code> parameter while creating a new inset axis:
    <code>ax.inset_ax(..., xlim=[1, 3])</code>
</div>

<div class="hint" title="How to set the inset axes ticks?">
    To set the inset axes ticks, you can use the <code>set_xticks</code> or <code>set_yticks</code> method of the <code>Axes</code> object:
    <code>inset_ax.set_xticks([1, 2, 3])</code>.<br><br>
    You can also set these ticks by passing the <code>xticks</code> or <code>yticks</code> parameter while creating a new inset axis:
    <code>ax.inset_ax(..., xticks=[1, 2, 3])</code>
</div>

<div class="hint" title="How to connect the inset axes with the parent axes area?">
    To connect the inset axes with the parent axes area, you can use the <code>indicate_inset_zoom</code> method of the <code>Axes</code> object:
    <code>ax.indicate_inset_zoom(inset_ax)</code>
</div>
