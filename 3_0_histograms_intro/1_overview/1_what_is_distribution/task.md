Histograms are great for visualizing the distribution of 1D continuous data.
They divide the value range into bins, 
making it easy to spot clusters, skewness, and outliers.
This makes them especially useful for large datasets,
offering a quick overview without needing to inspect each data point.

Scatter plots can also show distribution, particularly in 2D or 3D.
For 1D data, they’re less effective at showing density but are useful for spotting outliers.
Reducing point opacity helps approximate density—darker areas indicate more overlap.
That’s why scatter plots often follow histograms in deeper analysis.

When Jonsi was offered a promotion, his task appeared straightforward: 
analyze city rainfall data -- crucial for planning upgrades to the drainage system and preventing floods.
He initially tried to create a scatter plot to examine the distribution.
Jonsi added a bit of jitter to prevent the precipitation data from collapsing into a single line.
This revealed one outlier and a region where the data appeared fairly evenly distributed, 
which struck him as strange. 
He then recalled that histograms are better suited for this kind of analysis. 
After plotting one, he realized the data wasn’t uniform at all: the data clustered around specific rainfall levels.
This insight exposed the actual thresholds where the drainage system failed.
