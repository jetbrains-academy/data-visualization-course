## Goal

The main goal of the lesson is to **plot descriptive statistics about different game platforms and their global sales**:
1. Number of different platforms (as a bar chart and pie chart)
2. Total sales per decade for each region

## Theory

In Matplotlib, there are several functions for plotting categorical charts:
1. [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar) — Builds vertical bar charts.
2. [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html#matplotlib.pyplot.barh) — Similar to `bar` but builds horizontal bar charts.
3. [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie) — Builds pie charts.

For now, we will start with the `bar` function.

Like other Matplotlib functions, `bar` accepts three main arguments: 
`x`, `height` (similar to `y` in other plot types), and `data`.
We described them in detail in the 
"[Line and Scatter Plots](course://1_2_line_and_scatter_plots_matplotlib/1_theory/1_scatter)" section.

Unfortunately, Matplotlib doesn't aggregate the data for us, so we need to do it manually.

## Task

1. Use the hidden `aggregate` function to calculate the number of games (`count`)
   for each platform (`platform`) in descending order.

   If you prefer, you can aggregate the data yourself. Please refer to the corresponding hint below.

2. Call the `bar` method of `Axes` object to plot a bar chart. 
   Set `platform` as the x-axis, `count` as the height and `games` as the data.

Note that we have preprocessed the data for you. To learn how we do it, refer to the corresponding hint below.

## Hints
<div class="hint" title="How to run the code?">
   To run the code, click the green triangle next to the entry point.
   If there are any execution errors, they will be displayed in the console inside the IDE. 
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="How to import hidden functions?">
    To import it, you can place the cursor on the underlined hidden function name in your code, then press &shortcut:ShowIntentionActions;, and
    select <samp>Import 'function_name from data'</samp>:
   <img src="../../../common/resources/images/common/hidden_function_import.gif" alt="How to import hidden functions" style="max-height: 500px">
</div>

<div class="hint" title="Where to find my figure?">
   After running the code, the graph will be generated next to the <code>task.py</code> file.
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="How was the data preprocessed?">
   Before using the data, we need to perform several preprocessing steps:
   <ol>
      <li>Convert column names to lowercase.</li>
      <li>Drop all NaN values from the following columns:</li>
      <ul>
         <li><code>platform</code></li>
         <li><code>year_of_release</code></li>
         <li><code>global_sales</code></li>
         <li><code>eu_sales</code></li>
         <li><code>jp_sales</code></li>
         <li><code>na_sales</code></li>
         <li><code>other_sales</code></li>
      </ul>
      <li>Convert the <code>year_of_release</code> column to an integer.</li>
   </ol>
</div>

<div class="hint" title="How should I aggregate the data?">
   To calculate the total number of games per platform: 
   <ol>
      <li>Use the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html"><code>value_counts</code></a> method on the <code>platform</code> column to calculate the number of rows for each platform.</li>
      <li>Convert the result into <code>DataFrame</code> using the <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html"><code>reset_index</code></a> method.</li>
   </ol>

   Note that your custom function will not be tested.
</div>

<div class="hint" title="What should the figure look like?"> 
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
