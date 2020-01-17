# fout = open('foo.txt', 'wt')
# print('I created a file', file=fout)
# fout.close()

import os

file_name = 'foo.txt'

result = os.path.exists(file_name)
print(result)

result = os.path.isfile(file_name)
print(result)

result = os.path.isdir(file_name)
print(result)

result = os.path.abspath(file_name)
print(result)
