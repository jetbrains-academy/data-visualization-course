## Theory

This is slightly better, but it is still not convenient for exploration.
To more easily understand which platforms are more popular, we can reorder them.

The order of categories is controlled by the `order` argument.
It accepts a list of category names that specifies the desired display order.

## Task

Use the hidden `get_sorted_platforms` function
to get the list of platforms in ascending order, and pass it to the `catplot` function.

If you prefer, you can sort the platforms manually. Please refer to the corresponding hint below.

## Hints

<div class="hint" title="What should the figure look like?">
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>

<div class="hint" title="How to import hidden functions?">
    To import it, you can place the cursor on the underlined hidden function name in your code, then press &shortcut:ShowIntentionActions;, and
    select <samp>Import 'function_name from data'</samp>:
    <img src="../../../common/resources/images/common/hidden_function_import.gif" alt="How to import hidden functions" style="max-height: 500px">
</div>

<div class="hint" title="How should I sort the platforms?">
    To sort the platforms, you can use
    the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html"><code>value_counts</code></a> method
    on the <code>platform</code> column:
    <ol>
        <li>Pass the <code>sort</code> argument, along with <code>ascending</code>.</li>
        <li>Then, use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html"><code>index</code></a> property to retrieve the sorted platform names.</li>
        <li>Finally, convert the <code>Index</code> object to a list using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Index.to_list.html"><code>to_list</code></a> method.</li>
    </ol>
</div>
