import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CURR_DIR = os.path.dirname(__file__)

# データの読み込み
df = pd.read_csv(CURR_DIR + '/../data/iris.csv')

# SepalLength列をndarrayに変換
data = np.array(df['SepalLength'])

# ヒストグラム
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(data, bins=10, histtype='barstacked', ec='black')
plt.show()
