import numpy as np
from scipy import stats

np.random.seed(5)
normal_data  = np.random.normal(0, 1, 500)
skewed_data  = np.random.exponential(1, 500)

for name,data in [("Normal", normal_data),("skewed", skewed_data)]:
    jb_stat,jb_pvalue = stats.jarque_bera(data)
    print(f"{name} data: jarque_bera stat = {jb_stat:.3f}, p-value = {jb_pvalue:.3f}"
    f"{' Normal' if jb_pvalue > 0.05 else ' Not Normal'}")    

