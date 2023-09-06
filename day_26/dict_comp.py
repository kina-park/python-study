# # Dictionary Comprehension
#
# new_dict = {new_key : new_value for item,in list}
# new_dict = {new_key : new_value for (key, value),in dict.itmes()}
# new_dict = {new_key : new_value for (key, value),in dict.itmes() if test}

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# students_score = {student:random.randint(1, 100) for student in names}
# print(f"students_score: {students_score}")
# passed_students = {student:score for (student, score) in students_score.items() if score > 50}
# print(f"passed_students: {passed_students}")

# # Exercise_1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

# Exercise_2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: temp*9/5+32 for (day, temp) in weather_c.items()}
print(weather_f)


