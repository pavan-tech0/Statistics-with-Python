import numpy as np

datasets = {
    "Group A": [10, 15, 14, 16, 17, 18, 20, 22, 55],
    "Group B": [5,  12, 13, 14, 15, 16, 17, 18, 19],
}

print(f"{'Metric':<12} {'Group A':>10} {'Group B':>10}")
print("-" * 34)

metrics = [("Min", np.min), ("Q1", lambda x: np.percentile(x, 25)), ("Median", np.median),

             ("Q3", lambda x: np.percentile(x, 75)), ("Max", np.max), ("IQR", lambda x: np.percentile(x,75) - np.percentile(x,25))]
for name, func in metrics:
    val_a = func(datasets["Group A"])
    val_b = func(datasets["Group B"])
    print(f"{name:<12} {val_a:>10.2f} {val_b:>10.2f}")

#Boxplot visualization
import matplotlib.pyplot as plt
plt.figure (figsize=(8,6))
plt.boxplot([datasets["Group A"], datasets["Group B"]], labels=["Group A", "Group B"], patch_artist=True)
plt.title("Box Plot Comparison")
plt.ylabel("Values")
plt.grid(axis='y')
plt.show()
