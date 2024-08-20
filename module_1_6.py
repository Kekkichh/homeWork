my_dict = {'Name': 'Николай', 'Date_of_Birdh': 2002}
print(my_dict)
print(my_dict.get('Name'))
print(my_dict.get('Vlad', 'Такого ключа нет'))
my_dict.update({'Alex': 232323232323,
                'Kama': 32423423423})
print(my_dict)
a = my_dict.pop('Name')
print(my_dict)
print(a)

my_set = {1, 2, 3, 1, 2, 3}
print(my_set)
my_set.update({'apple', 123})
my_set.discard(1)
print(my_set)
