# # for loop
# numbers = [1, 2, 3]
# new_numbers = []
# for n in numbers:
#     new_n = n + 1
#     new_numbers.append(new_n)
#
# # List comprehension
# # new_list = [new_item for item in list]
#
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# Python Sequences - list, range, string, tuple
# 명확하게 순서를 갖고 있다는 특징.
# 그래서 list comprehension을 사용하게 되면 시퀀스를 써서 순서대로 통과하게 됨

# print([i*2 for i in range(1, 5)])

# Conditional List Comprehension
# new_list = [new_item for item in list if test]

# names = ["Alex", "Beth", "Caroline", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) <= 4]
# upper_names = [name.upper() for name in names if len(name) > 5]

# # Exercise.1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

# # Exercise.2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n%2 == 0]
# print(result)

# # Exercise.3
# with open("file1.txt") as file1:
#     numbers = file1.readlines()
#     print(numbers)
#     numbers1 = [num.strip('\n') for num in numbers]
#
# with open("file2.txt") as file2:
#     numbers = file2.readlines()
#     print(numbers)
#     numbers2 = [num.strip('\n') for num in numbers]
#
# print(numbers1)
# print(numbers2)
#
# print([int(num) for num in numbers1 if num in numbers2])

