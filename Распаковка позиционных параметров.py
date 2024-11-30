def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params('dfd', 2, '8')
print_params(c=41)
print_params(a=[1,2,3])

values_list = [22, 'СТРОЧКА', False]
value_dict = {'a': values_list[0], 'b': values_list[1], 'c': values_list[2]}

print_params(value_dict)
print_params(*value_dict)
print_params(**value_dict)

values_list_2 = [33, 'ЛиниЯ']

print_params(values_list_2)
print_params(*values_list_2, 55)