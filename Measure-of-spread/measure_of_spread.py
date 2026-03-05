import numpy as np
import pandas as pd
from scipy import stats
import random

data = [random.randint(1,70) for _ in range(25)]
print(f"Data: {data}")

# Range
print(f"Range: {np.ptp(data)}")                        # Peak-to-peak (range)

# IQR
Q1, Q3 = np.percentile(data, [25, 75])
print(f"IQR: {Q3 - Q1}")

# Variance
print(f"Variance (Population): {np.var(data)}")
print(f"Variance (Sample): {np.var(data, ddof=1)}")

# Standard Deviation
print(f"Standard Deviation (Population): {np.std(data)}")
print(f"Standard Deviation (Sample): {np.std(data, ddof=1)}")

# CV
mean, std = np.mean(data), np.std(data, ddof=1)
cv = (std / mean) * 100
print(f"CV: {cv:.2f}%")

# Z-scores
z_scores = stats.zscore(data)
print(f"Z-scores: {z_scores}")

# MAD
mad = np.mean(np.abs(data - np.mean(data)))
print(f"MAD: {mad}")
