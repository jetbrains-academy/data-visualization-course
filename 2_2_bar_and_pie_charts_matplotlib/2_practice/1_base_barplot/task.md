## Task

At a recent tasting event, participants were invited to sample an assortment of breads, cheeses, and salads.
Everyone had the chance to vote for up to 3 products per category, sharing their favorites from the diverse offerings.
The organizers collected all the responses and
calculated the percentage of votes for each product within each category
(to understand the distribution across bread, cheese, and salad).
Now they want us to help with plotting the data.
Let's help them!

To interpret the data,
the organizers want to see the distribution of votes (`votes`) for each category (`category`) in a single horizontal bar
chart.
So, you should plot the categories from top to bottom in the same order as they appear in the data
and color them accordingly:
`bread` - `sienna`, `cheese` - `goldenrod`, `salad` - `forestgreen`.

Y-axis requirements:

1. Each bar should have the corresponding product name on the left side (i.e. `cheddar`).
2. Set the y-axis label to `Product name`.
3. Product names within each category should be sorted in alphabetical order (from top to bottom).

X-axis requirements:

1. The x-axis should have only these ticks: `0`, `25`, `50`, `75`, and `100`.
2. Set the x-axis label to `Respondents, %`.

You should also make some visual adjustments to the figure:

1. Set the chart title to `Distribution of votes per category`.
2. Add a legend.
3. Tighten the layout.

Note that we've preprocessed the data for you. To learn how we did it, refer to the corresponding hint below.

You can use the following hidden functions:

1. `get_category_product_names`: Retrieves all product names for a specific category in alphabetical order (from top to bottom).
2. `get_category_votes`: Retrieves all votes for a specific category in the same order as the product names.
3. `get_category_size`: Calculates the number of products in a specific category.
4. `get_categories`: Retrieves a list of all categories in the order they appear in the data.

If you get stuck, please feel free to use the hints below, where you can also find what the final figure should look
like.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I preprocess the data?">
   Before using the data, we need to perform several preprocessing steps:
   <ol>
      <li>Calculate the number of votes for each category and product using
      the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html"><code>groupby</code></a>
      and <a href="https://pandas.pydata.org/docs/reference/api/pandas.core.groupby.DataFrameGroupBy.count.html"><code>count</code></a> methods.</li>
      <li>Normalize the data by dividing it by the number of participants, then multiply it by 100 to get the percentage.
      We can find the number of participants using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html"><code>nunique</code></a> method.</li>
      <li>Rename the <code>participants</code> column to <code>votes</code> using
      the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html"><code>rename</code></a> method.</li>
      <li>Reset the index using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html"><code>reset_index</code></a> method.</li>
   </ol>
</div>

<div class="hint" title="How to set the colors for the bars?">
    To set the colors for the bars, you can use the <code>color</code> argument of the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html"><code>barh</code></a> method:
    <code>ax.barh(positions, values, color="red")</code>
</div>

<div class="hint" title="How to set the labels for the products?">
    To set the labels for the products, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html"><code>set_yticks()</code></a> method:
    <code>ax.set_yticks([1, 2, 3], ["cucumber", "carrot", "tomato"])</code>
</div>

<div class="hint" title="How to limit the x-axis?">
    To limit the x-axis view, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html"><code>set_xlim</code></a> method:
    <code>ax.set_xlim(1, 3)</code>.
</div>

<div class="hint" title="How to set ticks for the x-axis?">
    To set ticks for the x-axis, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html"><code>set_xticks</code></a> method:
    <code>ax.set_xticks([1, 2, 3])</code>.
</div>

<div class="hint" title="How to set a label for an axis?">
    To set a label for an axis,
    you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html"><code>set_xlabel</code></a>
    or <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html"><code>set_ylabel</code></a> method:
    <code>ax.set_xlabel("x")</code>.
</div>

<div class="hint" title="How to set the figure title?">
    To set the figure title, you can use the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html"><code>set_title</code></a> method:
    <code>ax.set_title("Title")</code>.
</div>

<div class="hint" title="How to add a legend?">
    To add a legend, you should call the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html"><code>ax.legend</code></a> method.
</div>

<div class="hint" title="How to tighten the layout?">
    To tighten the layout, you should call the <a href="https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html"><code>fig.tight_layout</code></a> method.
</div>
