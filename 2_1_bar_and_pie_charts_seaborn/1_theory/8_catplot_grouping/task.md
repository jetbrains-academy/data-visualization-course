## Theory

It is interesting to note that the total global sales were lower in the 2010s compared to the 2000s.
It is probably because the data for games from the 2010s is incomplete.

Another advantage of bar charts is that we can easily include an additional category in the analysis.
For example, if we want to distinguish the most popular sales regions for each decade,
we can achieve this using the `hue` argument.
It can create separate bars for each region, color them differently, and place them side by side for each decade.
If it sounds too complicated, let's jump into the task to see how it works in practice!

## Task

1. Use the hidden `extract_sales_region` function to extract sales region data and values
   from the `eu_sales`, `jp_sales`, `na_sales`, and `other_sales` columns.
   
   This function unpivots the data, creating four new rows for each game and adding two new columns:
   `region` (which can be `eu`, `jp`, `na`, or `other`) and `sales`.

   If you prefer, you can extract the regions manually. Please refer to the corresponding hint below.

2. Plot the `sales` column on the y-axis instead of `global_sales`.
3. Pass the `region` value to the `hue` argument. 


## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I plot the total global sales?">
   To plot the total global sales, you should use the <code>estimator</code> argument 
   and pass the <code>sum</code> value.
</div>

<div class="hint" title="How should I extract the regions?">
    To extract the regions, you could use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.melt.html"><code>melt</code></a> function.
</div>
