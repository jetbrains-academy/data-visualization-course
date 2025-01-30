## Theory

Let's start by analyzing how video game sales are distributed in our dataset. The simplest way to visualize this distribution using Seaborn is with the `histplot` function.

The `histplot` function works similarly to other Seaborn plotting functions we've used before, accepting:
- `data`: The input DataFrame
- `x` or `y`: The column to plot (use `x` for vertical bars, `y` for horizontal bars)
- Various optional parameters to customize the appearance

## Task

Create a histogram showing the distribution of global sales using the `histplot` function. Pass the `games` DataFrame as `data` and use the `global_sales` column for the x-axis.

## Hints

<div class="hint" title="How to run the code?">
   To run the code, click the green triangle next to the entry point.
   In case of execution errors, they will be displayed in the console inside the IDE. 
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="Where to find my figure?">
   After running the code, the graph will be generated next to the `task.py` file.
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
