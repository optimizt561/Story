# my_list = [1, 2, 3, 4, 5, 6, 7]
# newlist = [n+1 for n in my_list]
# print(newlist)

# lis = [n*2 for n in range(2, 10)]
# print(lis)

# name = 'Angela'
# new = [n for n in name]
# print(new)

#
# names = ['Alex', 'eleanor', 'Dave', 'Joseph', 'Beth', 'Esther']
# short = [n for n in names if len(n) < 5]
# print(short)
#
# nam = [n.upper() for n in names if len(n) > 5]
# print(nam)



# #For Loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# #List Comprehension
# new_list = [n + 1 for n in numbers]
#
# #String as List
# name = "Angela"
# letters_list = [letter for letter in name]
#
# #Range as List
# range_list = [n * 2 for n in range(1, 5)]
#
# #Conditional List Comprenhension
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
#
# upper_case_names = [name.upper() for name in names if len(name) > 4]
#
# #Dictionary Comprehension
# import random
# student_grades = {name: random.randint(1, 100) for name in names}
# print(student_grades)
#
# passed_students = {
#     student: grade
#     for (student, grade) in student_grades.items() if grade >= 60
# }
# print(passed_students)


# list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# new = [n**2 for n in list]
# print(new)


number = ['1', '1', '2', '3', '5', '8', '13', '23', '34', '55']
intnum = [int(n) for n in number]
print(intnum)
result = [n for n in intnum if n % 2 == 0]
print(result)











