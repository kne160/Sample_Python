'''
Created on 16 Jan 2020

@author: kne16
'''
fin = open('sample.txt', 'rt')
count = 0
while True:
    line = fin.readline()
    if not line:
        break
    count += 1
    print(count, ':', line)

fin.close()
