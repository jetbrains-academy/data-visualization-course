## Theory

Here we can see that we have many platforms in the dataset,
which makes the figure difficult to interpret due to overlapping labels on the x-axis.
We can address this issue either by reducing the number of groups 
or by adjusting the layout of the figure, relocating labels from the x-axis to the y-axis.

Seaborn makes it easy to change the layout: we just need to swap `x` and `y`. 
However, for a count plot, we need to replace `x` with `y` (or vice versa),
as this kind of plot accepts only one axis at a time.

## Task

Adjust the figure's layout by replacing the x-axis with the y-axis.

## Hints

<div class="hint" title="What should the figure look like?">
   Please note that your figure might look slightly different due to the way Seaborn calculates error bars.

   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
