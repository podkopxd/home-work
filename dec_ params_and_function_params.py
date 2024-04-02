def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [16, 'is', True]
values_dict = {'a': False, 'b': 15, 'c': 'jun'}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [18, 'num']


print_params(42, *values_list_2)