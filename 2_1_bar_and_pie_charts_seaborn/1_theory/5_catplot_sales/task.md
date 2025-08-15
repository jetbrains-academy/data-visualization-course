## Theory

Now that we've explored the popularity of platforms, let's look at global sales across some platforms.
To do this, we can continue using `catplot`, but this time with a different kind – `bar`.

As we saw in the previous charts, we have a lot of game platforms, including some "ancient" ones.
To simplify our analysis, let's focus only on the most modern platforms: `PS4`, `PC`, `XOne`, and `WiiU`. 

## Task

1. Use the hidden `filter_platforms` function to filter out older game platforms.

   If you prefer, you can filter the platforms manually. Please refer to the corresponding hint below.

2. Change the `kind` argument to `bar` and plot `global_sales` on the y-axis.

Please note that you don't need to specify the `order` and `stat` arguments,
and that the bar chart should now use the vertical layout.

## Hints

<div class="hint" title="What should the figure look like?">
   Please note that your figure might look slightly different due to the way Seaborn calculates error bars. 
   
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I filter the platforms?">
    To filter out the unnecessary platforms, you can use
    the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html"><code>isin</code></a> method
    on the <code>platform</code> column.
</div>
