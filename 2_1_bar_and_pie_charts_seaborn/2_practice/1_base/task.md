## Task

At a recent tasting event, participants were invited to sample an assortment of breads, cheeses, and salads.
Everyone had the chance to vote for up to three products per category,
sharing their favorites from the diverse offerings.
The organizers of the event have collected all the responses and now need our help in plotting the data.
Let's help them!

To interpret the data,
the organizers want to see the distribution of votes for each category (`category`) in a single horizontal bar
chart.
You need to plot the categories from top to bottom in the same order as they appear in the data: `bread`, `cheese`, and `salad`.

The other requirements are:

1. The bar chart should be horizontal.
2. The bars should be grouped by category.
3. Product names within each category should be sorted in alphabetical order (from top to bottom).
4. The bar chart should include a legend.

Note that you don't need to preprocess the data.

You can use the hidden `get_product_order` function to get the correct product order if needed.

If you get stuck, please feel free to use the hints below, where you can also find what the final figure should look
like.

## Further customization

If you want, you can further customize the figure. Here are some ideas for customization:

1. Adjust font weights and sizes.
2. Move the legend items to the y-axis.
3. Add a corresponding numeric value at the top of each bar. 

We encourage you to explore these customizations on your own, as not all of them will be covered in the course.

Note that these changes will not be tested and may cause existing tests to break.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="Which bar chart type should I use?">
    As we need to plot the distribution of votes, the best choice is to use a <a href="https://seaborn.pydata.org/generated/seaborn.catplot.html">count plot</a>: 
    <code>sns.catplot(..., kind="count")</code>
</div>

<div class="hint" title="How to make a bar horizontal?">
    To make a bar horizontal, you can change the <code>x</code> argument to <code>y</code>.
</div>

<div class="hint" title="How to group the bars by category and add a legend?">
    To group the bars by category and add a legend, you can use the <code>hue</code> argument.
</div>

<div class="hint" title="How to change the order of the products?">
    To change the order, you could use the <code>order</code> argument.
</div>
