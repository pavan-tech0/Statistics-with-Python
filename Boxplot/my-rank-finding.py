import numpy as np
from scipy import stats

# Sample dataset

scores = np.array([45, 50, 55, 60, 65, 70, 72, 75,
                   78, 80, 82, 85, 90, 92, 95, 98])

my_score = 76

# Calculate ramk from scores
rank = stats.percentileofscore(scores, my_score, kind='rank')


bands = {0: "F", 50: "D", 60: "C", 75: "B", 90: "A"}

print("\n Score Bands:")
for grade, pct in bands.items():
    cutoff= np.percentile(scores, grade)
    print(f"  {grade:>3} → {pct} >= {cutoff:.2f}")

# Find the correct grade for my_score
grade_for_my_score = None
for cutoff, grade in sorted(bands.items()):
    if my_score >= cutoff:
        grade_for_my_score = grade
# Print result with correct grade
print(f"My score: {my_score} --> Rank: {rank:.2f}% --> Grade: {grade_for_my_score:>3}")

