'''
Created on 17 Jan 2020

@author: kne16
'''

import scipy as sp
import numpy as np

data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")

print(data[:10])
print(data.shape)

x = data[:, 0]
y = data[:, 1]

print(np.sum(np.isnan(y)))

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.title('Web traffic over the last month')
plt.xlabel('Time')
plt.ylabel('Hits/hour')
plt.xticks([w * 7 * 24 for w in range(10)],
           ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
# plt.show()


def error(f, x, y):
    return np.sum((f(x) - y) ** 2)


fp1, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full=True)

print("Model parameters: %s" % fp1)
print(residuals)

f1 = sp.poly1d(fp1)
print(error(f1, x, y))

fx = np.linspace(0, x[-1], 1000)  # プロット用に"x"値を生成
plt.plot(fx, f1(fx), linewidth=1)
plt.legend(["d=%i" % f1.order], loc="upper right")
# plt.show()

f2p = np.polyfit(x, y, 2)
print(f2p)

f2 = np.poly1d(f2p)
print(error(f2, x, y))

inflection = 3.5 * 7 * 24  # 変化点(急に変化する点)の時間を計算

# 変化点前のデータポイント
xa = x[:int(inflection)]
ya = y[:int(inflection)]

# 変化点後のデータポイント
xb = x[int(inflection):]
yb = y[int(inflection):]

fa = sp.poly1d(np.polyfit(xa, ya, 1))
fb = sp.poly1d(np.polyfit(xb, yb, 1))

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)
print("Error inflection=%f" % (fa_error + fb_error))

frac = 0.3  # テストに用いるデータの割合
split_idx = int(frac * len(xb))

# 全データの30%をランダムに選び出す
shuffled = sp.random.permutation(list(range(len(xb))))
test = sorted(shuffled[:split_idx])  # テスト用のデータインデックス配列
train = sorted(shuffled[split_idx:])  # 訓練用のデータインデックス配列

# それぞれの訓練データを用いて訓練を行う
fbt1 = sp.poly1d(np.polyfit(xb[train], yb[train], 1))
fbt2 = sp.poly1d(np.polyfit(xb[train], yb[train], 2))
fbt3 = sp.poly1d(np.polyfit(xb[train], yb[train], 3))
# fbt10 = sp.poly1d(np.polyfit(xb[train], yb[train], 10))
# fbt100 = sp.poly1d(np.polyfit(xb[train], yb[train], 100))

for f in [fbt1, fbt2, fbt3]:
    print("Error d=%i: %f" % (f.order, error(f, xb[test], yb[test])))

print(fbt2)
print(fbt2 - 100000)

from scipy.optimize import fsolve
reached_max = fsolve(fbt2 - 100000, 800) / (7 * 24)
print("100,000 hits/hour expected at week %f" % reached_max[0])

