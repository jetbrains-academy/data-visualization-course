## Theory

This visualization is much better, as we can now identify the big dense cluster in our dataset.
Moreover, we can observe a potential linear relationship between the two scores.
To explore this further, let's attempt a linear approximation of the data.

As mentioned before, `relplot` can build not only scatter plots but also line plots.
To specify the type of plot, we can use the `kind` parameter,
which accepts one of the following strings: `scatter` for scatter plots and `line` for line plots.
In the previous steps, there was no need to explicitly set this parameter to `scatter`
because that is its default value.

## Task

Make `relplot` build a line plot. Note that you don't need to adjust the transparency or change the color for this plot.

## Hints
<div class="hint" title="What should the figure look like?">
  <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
