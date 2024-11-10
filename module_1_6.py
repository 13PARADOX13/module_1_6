from winreg import DeleteValue

my_dict = {'Anton': 1987, 'Semen': 1991, 'Artem': 2000}
print('my_dict', my_dict)
print('Existing value: ', my_dict['Semen'])
print('Not existing value: ', my_dict.get('Dasha'))
my_dict.update({'Masha': 1999, 'Viktor': 2002})
Deleted_value = my_dict.pop('Anton')
print('Deleted value: ', Deleted_value)
print('Modified my_dict:', my_dict)

my_set = {1, 2, 2, 3, 3, 3, 'zx', 'xz', 'cx', 'zx', 'xz'}
print('my_set: ', my_set)
my_set.update({'asd', (0.75, 1.25)})
my_set.discard('cx')
print('Modefied set: ', my_set)