from timeit import timeit

def make_list_slower():
    result = []
    for value in range(1000):
        result.append(value)
    return result

def make_list_faster():
    result = [value for value in range(1000)]
    return result

print('make_list_slower', timeit(make_list_slower, number=1000), 'seconds')
print('make_list_faster', timeit(make_list_faster, number=1000), 'seconds')
