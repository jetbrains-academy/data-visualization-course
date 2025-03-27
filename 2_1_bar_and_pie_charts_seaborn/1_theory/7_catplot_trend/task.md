## Theory

So far, we have plotted continuous values (global sales) for each of the categorical values (platforms).
But what if we have two continuous variables?
More precisely, what do we do if we want to compare global sales across different years?

We can do this using a line plot. 
However, if the number of possible categories is small (for example, if we look only at decades),
a bar chart is also suitable for this purpose.

## Task

Use the hidden `add_decades` function to add a new `decade` column to the data 
and plot the _**total**_ global sales by decade.

Please note that you don't need to reorder the columns, as they are sorted automatically.

If you prefer, you can add the decades manually. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I plot the total global sales?">
   To plot the total global sales, you should use the <code>estimator</code> argument 
   and pass the <code>sum</code> value.
</div>

<div class="hint" title="How should I add the decades?">
    To add the decades, you could use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.cut.html"><code>cut</code></a> function.
</div>
