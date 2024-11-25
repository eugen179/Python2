def find_largest_number(numbers):

  if not numbers:
    return None

  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  return largest

my_list = [3, 7, 2, 9, 5]
result = find_largest_number(my_list)
print(result)  