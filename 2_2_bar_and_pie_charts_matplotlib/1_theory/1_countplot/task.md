## Goal

The main goal of the lesson is to **plot the descriptive statistics about different game platforms and global sales**:
1. Number of different platforms (as bar chart and pie chart)
2. Total sales per decade for each region

## Theory

In Matplotlib there are several functions for plotting categorical charts:
1. [`bar`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar): it builds vertical bar charts.
2. [`barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.barh): it is similar to `bar` but builds horizontal bar charts.
3. [`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.pie): it builds pie charts.

For now, we will start with the `bar` function.

As other Matplotlib functions, `bar` accepts three main arguments: 
`x`, `height` (similar to `y` in other plot types) and `data`.
We described them in detail in the 
"[Line and Scatter Plots](course://1_2_line_and_scatter_plots_matplotlib/1_theory/1_scatter)" section.

Unfortunately, Matplotlib doesn't aggregate the data for us, so we need to do it ourselves.

## Task

1. Use the hidden `aggeregate` function to calculate the number of games (the `count` column)
   for each platform (the `platform` column) in descending order.
   
   If you prefer, you can aggregate the data yourself. Please refer to the corresponding hint below.

2. Use the `bar` function to plot bar chart. 
   Pass `platform` there as the x-axis, `count` as the height and `games` as the data.

Note that we preprocessed the data for you, but if you prefer, you can do this yourself.
Please see the corresponding hint below.

## Hints
<div class="hint" title="How to run the code?">
   To run the code, click the green triangle next to the entry point.
   In case of execution errors, they will be displayed in the console inside the IDE. 
   <img src="../../../common/resources/images/common/entry_point.png" style="max-width: 500px">
</div>

<div class="hint" title="Where to find my figure?">
   After running the code, the graph will be generated next to the <code>task.py</code> file.
   <img src="../../../common/resources/images/common/output_location.png" style="max-width: 500px">
</div>

<div class="hint" title="How should I preprocess the data?">
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
   
   If you have some difficulties with your own preprocessing, you can take
   [a peek at the inner file](file://2_2_bar_and_pie_charts_matplotlib/1_theory/1_countplot/data.py)
   where our preprocessing is defined.
</div>

<div class="hint" title="How should I aggregate the data?">
   To calculate the total number of games per platform: 
   <ol>
      <li>Count the number of rows for the <code>platform</code> column using <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html"><code>value_counts</code></a> function</li>
      <li>Convert the result to DataFrame using <a href="https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html"><code>reset_index</code></a> function</li>
   </ol>
   
   If you have some difficulties with your own preprocessing, you can take
   [a peek at the inner file](file://2_2_bar_and_pie_charts_matplotlib/1_theory/1_countplot/data.py)
   where our preprocessing is defined.
</div>

<div class="hint" title="What should the figure look like?"> 
   <img src="example.png" alt="What the figure should look like" style="max-height: 500px">
</div>
