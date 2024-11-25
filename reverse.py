def reverse_list(my_list):
  n = len(my_list)
  for i in range(n // 2):
    my_list[i], my_list[n-i-1] = my_list[n-i-1], my_list[i]

  return my_list

characters = ['a', 'b', 'c', 'd', 'e']
reversed_characters = reverse_list(characters)
print(reversed_characters) 