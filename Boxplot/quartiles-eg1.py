import numpy as np

exam_scores = [45, 55, 60, 62, 65, 68, 70, 72,
               75, 78, 80, 82, 85, 88, 92, 95]

percentiles = [10, 25, 50, 75, 90, 95]

print("Percentile → Value")
for p in percentiles:
    val = np.percentile(exam_scores, p)
    print(f"  P{p:>3}  →  {val}")

Q1, Q2, Q3 = np.percentile(exam_scores, [25, 50, 75])
IQR = Q3 - Q1
print(f"\nQ1={Q1}, Q2={Q2}, Q3={Q3}, IQR={IQR}")
