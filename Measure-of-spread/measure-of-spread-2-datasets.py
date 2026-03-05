import numpy as np
import random

a = [random.randint(1,30) for _ in range (15)]
b = [random.randint(1,60) for _ in range(15)]

for label, data in [("Dataset A", a),("Dataset B",b)]:
    arr = np.array(data)
    print(f"\n{label}")
    print(f"Mean  = {np.mean(data)}")
    print(f"Variance = {np.var(data,ddof=1)}")
    print(f"Range = {np.ptp(data)}")
    print(f"Standard Deviation = {np.std(data,ddof=1)}")
