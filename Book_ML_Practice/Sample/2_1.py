'''
Created on 17 Jan 2020

@author: kne16
'''

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
from sklearn.compose import _target

# データをロード
data = load_iris()

# print(data['DESCR'])

features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target]

for t, marker, c in zip(range(3), ">ox", "rgb"):
    # クラスごとに色の異なるマーカでプロットする
    plt.scatter(features[target == t, 0],
                features[target == t, 1],
                marker=marker,
                c=c)

# 花弁の長さは配列の3番目(インデックスは2)に格納されている
plength = features[:, 2]
is_setosa = (labels == 'setosa')  # setonaかどうかのブーリアン配列


max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

print('Maximum of setosa: {0}.'.format(max_setosa))
print('Maximum of others: {0}.'.format(min_non_setosa))

def apply_model(example):
    if example[2] < 2: print('Iris Setosa')
    else: print('Iris Virginica or Iris Vesicolor')

features = features[~is_setosa]
labels = labels[~is_setosa]
virginica = (labels == 'virginica')

best_acc = -1.0
best_fi = -1.0
best_t = -1.0

for fi in range(features.shape[1]):
    # 各特徴量ごとに閾値の候補を生成する
    thresh = features[:, fi].copy()
    thresh.sort()
    
    # 全ての閾値でテストする
    for t in thresh:
        pred = (features[:, fi] > t)
        acc = (labels[pred] == 'virginica').mean()
        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t

