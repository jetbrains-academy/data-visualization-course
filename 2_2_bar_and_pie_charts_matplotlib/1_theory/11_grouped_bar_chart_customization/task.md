## Theory

Now we can distinguish the traces, but the decade labels are missing.
To add them, we can use the familiar [`ax.set_xticks`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html) method.

Previously we only passed the positions where the ticks should be located. However,
we can also pass a second argument to this method — the labels for these ticks.
These labels will replace the numeric ones.

So let's go back to our example.
We need to place the labels at the center of each group.
As we can see from the picture, the center of the first group is located at `1.5`.
It is not hard to calculate other centers, as they are equally spaced apart by a distance of `group_size + 1`. 
<img src="../../../common/resources/images/bar_and_pie_charts/grouped-bar-chart-5.svg" style="max-height: 500px">

Also, let's add labels for the x-axis and y-axis, a title, and tighten the layout.

## Task

1. Add decade labels to the figure. 

   You can use the hidden `get_all_decades` function to get all decades.
   If you prefer, you can do it yourself. Please refer to the corresponding hints below.

2. Set the x-axis label to `Decade`.
3. Set the y-axis label to `Sales`.
4. Set the title to `Total sales for each region over decades`.
5. Tighten the layout.

## Hints

<div class="hint" title="How to set a label for an axis?">
    To set a label for an axis,
    you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html"><code>set_xlabel</code></a>
    or <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html"><code>set_ylabel</code></a> method:
    <code>ax.set_xlabel("x")</code>.
</div>

<div class="hint" title="How to set a title for a figure?">
    To set a title for a figure, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html"><code>set_title</code></a> method:
    <code>ax.set_title("Title")</code>.
</div>

<div class="hint" title="How to tighten the layout?">
   To tighten the layout, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html"><code>tight_layout</code></a> method: <code>fig.tight_layout()</code>.
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
