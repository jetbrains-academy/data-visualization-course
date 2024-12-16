## Task

At a recent tasting event, participants were invited to sample an assortment of breads, cheeses, and salads. Everyone
had the chance to vote for as many items as they liked, sharing their favorites among the diverse offerings. The
organizers of a tasting event received all the responses, calculated themselves the percentage of votes for each product
in each category (so that they know the corresponding distribution along cheese, bread and salad). Now they want us to
help
with plotting the data. Let's assist them!

In order to interpret the data, the organizers want to see the distribution of votes for each category at a single
horizontal bar chart. So you should plot categories from top to bottom as follows: `bread`, `cheese`, and `salad`.

The other requirements are:

1. The bars should be colored as follows: `bread` - `navy`, `cheese` - `firebrick`, `salad` - `green`.
2. Each bar should have the corresponding product label on the left side of the bar (i.e. `cheddar`).
3. Limit the x-axis view to the interval from `0` to `100`.
4. Remove ticks along the x-axis.
5. Label the x-axis as `Respondents, %`.
6. Set the chart title as `Respondents, %`.

Note that the width of each bar is `1` and the amount of product in each category is `5`. You also don't need to preprocess the data.

If you get stuck, please feel free to use the hints below, where you can also find what the final figure should look
like.

## Hints

<div class="hint" title="What should the figure look like?">
    <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to set the labels for the products?">
    You can use <code>ax.set_yticks()</code> and <code>ax.set_yticklabels()</code> methods to set the labels for the products.
</div>

<div class="hint" title="How to set the colors for the bars?">
    You can use the <code>color</code> argument of the <code>barh()</code> method to set the colors for the bars.
</div>

<div class="hint" title="How to remove x axis ticks?">
    You can use the <code>set_xticks()</code> method with an empty list to remove the x-axis ticks.
</div>
