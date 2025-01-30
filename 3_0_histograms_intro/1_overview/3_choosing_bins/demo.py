import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate skewed data
data = np.random.lognormal(mean=0, sigma=0.7, size=1000)

# Create figure with subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Effect of Bin Selection", fontsize=14)

# 1. Too few bins
ax1.hist(data, bins=5, alpha=0.7)
ax1.set_title("Too Few Bins (5)")

# 2. Sturges' rule
n_sturges = int(np.ceil(np.log2(len(data)) + 1))
ax2.hist(data, bins=n_sturges, alpha=0.7)
ax2.set_title(f"Sturges' Rule ({n_sturges} bins)")

# 3. Square root rule
n_sqrt = int(np.ceil(np.sqrt(len(data))))
ax3.hist(data, bins=n_sqrt, alpha=0.7)
ax3.set_title(f"Square Root Rule ({n_sqrt} bins)")

# 4. Too many bins
ax4.hist(data, bins=100, alpha=0.7)
ax4.set_title("Too Many Bins (100)")

# Adjust layout and save
plt.tight_layout()
plt.savefig("common/resources/images/histograms/3_bin_selection.png")
plt.close()
