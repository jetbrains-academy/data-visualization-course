## Theory

The figure looks good, but there is still one thing we can adjust - the ordering within each decade. 

The order of hue categories is controlled by the `hue_order` argument.
Similar to the `order` argument, it accepts a collection of category names to define the desired display order.

## Task

Use the hidden `get_sorted_regions` function to get the list of regions in descending order and pass it to the `catplot` function.

If you prefer, you can sort the platforms manually. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How should I sort the regions?">
    To sort the platforms, you can use
    the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html"><code>sort_values</code></a> method
    on the <code>platform</code> column:
    <ol>
        <li>Group the data by the <code>region</code> column.</li>
        <li>Calculate the sum of the <code>sales</code> column using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html"><code>sum</code></a> method.</li>
        <li>Sort the values using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html"><code>sort_values</code></a> method.</li>
        <li>Use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html"><code>index</code></a> property to retrieve the sorted platform names.</li>
        <li>Finally, convert the <code>Index</code> object to a list using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html"><code>to_list</code></a> method.</li>
    </ol>
</div>
