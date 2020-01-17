'''
Created on 17 Jan 2020

@author: kne16
'''
import numpy as np

print(np.version.full_version)

a = np.array([0, 1, 2, 3, 4, 5])
print(a)
print(a.ndim)
print(a.shape)

b = a.reshape((3, 2))
print(b)
print(b.ndim)
print(b.shape)

b[1][0] = 77
print(b)
c = a.reshape((3, 2)).copy()

print(a[np.array([2, 3, 4])])
print(a > 4)
print(a[a > 4])

a[a > 4] = 7
print(a)

print(a.clip(1, 3))

c = np.array([1, 2, np.NAN, 3, 4])
print(np.isnan(c))
print(c[~np.isnan(c)])
print(np.mean(c[~np.isnan(c)]))

import timeit

# normal_py_sec = timeit.timeit('sum(x*x for x in range(1000))',
#                               number=10000)
# naive_np_sec = timeit.timeit('sum(na*na)',
#                              setup="import numpy as np; na=np.arange(1000)",
#                              number=10000)
# good_np_sec = timeit.timeit('na.dot(na)',
#                             setup="import numpy as np; na=np.arange(1000)",
#                             number=10000)
#
# print("Normal Pyton: %f sec" % normal_py_sec)
# print("Naive Numpy: %f sec" % naive_np_sec)
# print("Good Numbpy: %f sec" % good_np_sec)

print(a.dtype)
print(np.array([1, "string"]).dtype)
print(np.array([1, "string", set([1,2,3])]).dtype)
