'''
Created on 16 Jan 2020

@author: kne16
'''

import re

source = 'This is a source message1'
result = re.findall('\d', source)
print(result)

result = re.findall('\w{4}', source)
print(result)
