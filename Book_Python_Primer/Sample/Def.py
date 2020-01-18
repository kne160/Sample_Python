'''
Created on 16 Jan 2020

@author: kne16
'''


def f_menu(dinner='fish'):
    print('D: ', dinner)


f_menu('bread')
f_menu()
print()


def f_args(arg1, arg2, *args):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('*args:', args)


f_args('foo', 'bar', 'more', 'and more')
print()


def f_kwargs(**kwargs):
    print('Keyword arguments: ', kwargs)


f_kwargs(breakfast='rice cake', lunch='pasta', dinner='beaf')
print()


def f_docstring(arg):
    '''
    This is a docstring sample
    @param: arg
    @return: arg

    '''
    return arg


help(f_docstring)
print()

print("__doc__")
print(f_docstring.__doc__)
print()

l_animals = ['Cat', 'Dog', 'Graff']


def f_story(words, func):
    for word in words:
        print(func(word))


f_story(l_animals, lambda word: word.capitalize() + '!')
print()


def f_document_it(func):

    def f_new(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)

        return result

    return f_new


@f_document_it
def f_add_ints(a, b):
    return a + b


# cooler_add_ints = f_document_it(f_add_ints)
# cooler_add_ints(3, 5)
f_add_ints(3, 5)
print()


def f_square_it(func):

    def f_new(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result

    return f_new


@f_document_it
@f_square_it
def f_add_ints2(a, b):
    return a + b


f_add_ints2(2, 3)
print()


class UppercaseException(Exception):
    pass


words = ['aaa', 'bbb', 'CCC']

def f_check(wordlist):
    for word in wordlist:
        if word.isupper():
            raise UppercaseException(word)


def f_Etest(wordlist):
    try:
        f_check(wordlist)
    except UppercaseException as err:
        print('Exception: ', err)

f_Etest(words)


