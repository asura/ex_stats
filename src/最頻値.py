# %%
import numpy as np
from scipy import stats

data = np.array([1, 2, 2, 3, 3, 5, 5, 5, 7, 7, 10])
m = stats.mode(data)

m.mode[0]  # 5

# %%
m.count[0]  # 3
