'''
Created on 16 Jan 2020

@author: kne16
'''
# comment line

alphabet = 'abc,' + \
'def,' + \
'ghi,' + \
'jkl'
print(alphabet)
print()

flag_t = True
if flag_t:
    print('if')
else:
    print('else')

if False:
    print('if')
elif flag_t:
    print('elif')
print()

list_empty = []
if list_empty:
    print("There's something in here")
else:
    print("It's a empty list")
print()

count = 1
while count <= 5:
    print('while loop: ', count)
    count += 1
print()

list_num = [1, 3, 5]
pos = 0
while pos < len(list_num):
    num = list_num[pos]
    if num % 2 == 0:
        print('even number:', num)
        break
    pos += 1
else:
    print('no even number')
print()

for count in range(5):
    print('for loop: ', count)
print()

list_empty = []
for item in list_empty:
    print('item: ', item)
    break
else:
    print('there is empty after for loop')
print()

list_days = ['Mon', 'Tue', 'Wed']
list_fruits = ['banana', 'orange', 'peach']
for day, fruit in zip(list_days, list_fruits):
    print('day: ', day, ', fruit: ', fruit)
print()

list_number = [num for num in range(1,5)]
print(list_number)
print()

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
print()

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")
print()
