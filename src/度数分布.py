import os

import numpy as np
import pandas as pd

CURR_DIR = os.path.dirname(__file__)

# データの読み込み
df = pd.read_csv(CURR_DIR + '/../data/iris.csv')

# SepalLength列をndarrayに変換
data = np.array(df['SepalLength'])

# ヒストグラム
hist, bin_edges = np.histogram(data, bins=10)
print(hist)
print(bin_edges)

# 表示用に整形する
hist_df = pd.DataFrame(columns=["start", "end", "count"])
for idx, val in enumerate(hist):
    start = round(bin_edges[idx], 2)
    end = round(bin_edges[idx + 1], 2)
    hist_df.loc[idx] = [start, end, val]
print(hist_df)
