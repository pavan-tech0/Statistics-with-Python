import numpy as np
import random

#data = np.array([random.randint(1,10000) for _ in range(10)])

data = np.array([14, 18, 101, 13, 6, 8, 2, 16, 150, 5,
                  9, 12, -50, 17, 15])


Q1, Q3 = np.percentile(data,[25,75])
IQR = Q3 - Q1

Lower_fence = Q1 - 1.5 * IQR
Upper_fence = Q3 + 1.5 * IQR

outliers = data[(data < Lower_fence) | (data > Upper_fence)]
print(f"Data: {data}")
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower Fence: {Lower_fence}, Upper Fence: {Upper_fence}")        
print(f"Outliers: {outliers}")

cleaned_data = data[(data>=Lower_fence) & (data<=Upper_fence)]
print(f"Cleaned Data: {cleaned_data}")
print(f"cleaned points are {len(cleaned_data)} out of {len(data)}")

