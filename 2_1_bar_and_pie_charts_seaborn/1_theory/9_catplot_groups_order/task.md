## Theory

The figure looks good but there is still one thing that we could justify - the ordering inside each decade. 

The order of hue categories is controlled by the `hue_order` argument.
As the `order` argument, it accepts a list of names in what order to show them.

## Task

Use the hidden `get_sorted_regions` function to get the list of regions in descending order and pass it to the `catplot` function.

If you prefer, you can sort the platforms yourself. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="How should I sort the regions?">
    To sort the platforms you can use
    the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html"><code>sort_values</code></a> function
    on the <code>platform</code> column:
    <ol>
        <li>Group the data by the <code>region</code> column.</li>
        <li>Calculate a sum using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html"><code>sum</code></a> function on the <code>sales</code> column.</li>
        <li>Sort values using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html"><code>sort_values</code></a> function</li>
        <li>After that, use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html"><code>index</code></a> property to receive sorted platform names.</li>
        <li>Finally, convert the <code>Index</code> object to a list using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html"><code>to_list</code></a> function.</li>
    </ol>
    
   If you have some difficulties with your own preprocessing, you can take
   [a peek at the inner file](file://2_1_bar_and_pie_charts_seaborn/1_theory/4_countplot_order/data.py)
   where our preprocessing is defined.
    
</div>

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
