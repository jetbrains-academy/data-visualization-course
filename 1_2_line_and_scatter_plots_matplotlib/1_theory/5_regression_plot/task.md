## Theory

Now we can definitely see an uptrend, but it is not a straight line.
How do we plot a straight line showing a trend?
For that, we can use a method called linear regression.
In simple terms, it attempts to draw a line through our data points in a way that minimizes the mean error.

The `aggregate` function now estimates the critic scores using the regression line.
If you'd like, you can implement this yourself.
Please see the corresponding hint below.

Previously, we used only one type of visualization, but what if we want to build a scatter plot along with the line?
With Matplotlib, we can easily do this—just
call another method from `Axes`, and it will be plotted on top of the previous ones.

For example, we can do it something like this:
```python
ax.plot("x1", "y1", data=my_data)
ax.scatter("x2", "y2", data=my_data)
```

## Task

Plot the regression line and add the scatter plot to it.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How does linear regression work?">
   Linear regression finds the best-fitting straight line through the data by minimizing the difference between 
   predicted and actual values. This is done by minimizing the squared errors between the line and the data points. 
   The equation of the line is: <code>y = mx + b</code>, where <code>m</code> is the slope and <code>b</code> is the
   intercept.
    
   Note again, that Matplotlib does not provide a built-in method for linear regression, 
   so you need to aggregate data yourself.
</div>

<div class="hint" title="How should I aggregate the data?">
   To aggregate the data, we can use NumPy:
   <ol>
      <li>Calculate the regression line coefficients using <a href="https://numpy.org/doc/stable/reference/generated/numpy.polyfit"><code>polyfit</code></a>. The degree of the fitting polynomial should be 1.</li>
      <li>Create a regression function using <a href="https://numpy.org/doc/stable/reference/generated/numpy.poly1d"><code>poly1d</code></a>. This function will accept <code>user_score</code> and return the approximate <code>critic_score</code>.</li>
      <li>Create a new DataFrame where the <code>user_score</code> column contains only unique values, and the <code>critic_score</code> is the result of applying the function from the second step to the new <code>user_score</code> column.</li>
   </ol>

   Note that your own aggregation function will not be tested.
</div>
