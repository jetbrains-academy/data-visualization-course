import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Create simulated temperature data for different months
# Simulate gradually warming temperatures from March to May
march_temps = np.random.normal(10, 3, 300)  # Colder
april_temps = np.random.normal(15, 4, 300)  # Warming up
may_temps = np.random.normal(20, 3, 300)    # Warmer

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
fig.suptitle("Spring Temperature Distributions:\nHistograms vs. Density Curves", fontsize=14)

# Plot histograms
months = ['March', 'April', 'May']
colors = ['#2E86C1', '#8E44AD', '#E67E22']
data = [march_temps, april_temps, may_temps]

# Top plot: Histograms
for temp, color, month in zip(data, colors, months):
    ax1.hist(temp, bins=15, alpha=0.5, color=color, label=month)
ax1.set_title("Using Histograms")
ax1.set_xlabel("Temperature (°C)")
ax1.set_ylabel("Count")
ax1.legend()

# Bottom plot: Density curves
for temp, color, month in zip(data, colors, months):
    sns.kdeplot(data=temp, ax=ax2, color=color, label=month, 
                fill=True, alpha=0.3, linewidth=2)
ax2.set_title("Using Density Curves")
ax2.set_xlabel("Temperature (°C)")
ax2.set_ylabel("Density")

# Add annotations
ax2.annotate('Smoother transitions\nbetween months', 
            xy=(15, 0.08), xytext=(16, 0.12),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax2.annotate('Overlapping patterns\nmore visible', 
            xy=(12, 0.02), xytext=(5, 0.04),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Adjust layout and save
plt.tight_layout()
plt.savefig("common/resources/images/histograms/3_density_curves.png")
plt.close() 