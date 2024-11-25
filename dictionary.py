dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = {'a': 1, 'b': 2}
dict4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

if dict1 == dict2 == dict3 == dict4:
    print("All dictionaries are identical.")
else:
    print("All dictionaries are not identical.")
is_subset_of_all = all(all(item in d.items() for item in dict1.items()) for d in [dict2, dict3, dict4])
if is_subset_of_all:
    print("dict1 is a subset of all other dictionaries.")
else:
    print("dict1 is not a subset of all other dictionaries.")
for i, d in enumerate([dict2, dict3, dict4], 2):
    if all(item in d.items() for item in dict1.items()):
        print(f"dict1 is a subset of dict{i}.")
    else:
        print(f"dict1 is not a subset of dict{i}.")
