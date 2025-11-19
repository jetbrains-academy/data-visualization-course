Histograms are great for visualizing the distribution of one-dimensional continuous data.
They divide the value range into bins, 
making it easy to spot clusters, skewness, and outliers.
This makes them especially useful for large datasets,
providing a quick overview without the need to inspect each data point.

Scatter plots can also show distribution, particularly in 2D or 3D.
For 1D data, however, they are less effective at showing density but are useful for spotting outliers.
Reducing point opacity helps approximate density—darker areas indicate more overlap.
That’s why scatter plots often complement histograms in deeper analysis.

When Jonsi was offered a promotion, his task seemed straightforward:
analyze city rainfall data, which was crucial for planning drainage system upgrades and preventing floods.
Initially, he created a scatter plot to examine the distribution.
To address the issue of precipitation data collapsing into a single line, Jonsi added a bit of jitter.
This revealed one outlier and a region where the data appeared fairly evenly distributed, 
which struck him as unusual.
He then recalled that histograms are better suited for this kind of analysis. 
After plotting a histogram, he realized the data wasn’t uniform at all: it clustered around specific rainfall levels.
This insight exposed the critical thresholds where the drainage system would fail.

<img src="../../../common/resources/images/histograms/distribution.svg">
