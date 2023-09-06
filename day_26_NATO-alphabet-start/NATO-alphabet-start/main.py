# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# import pandas as pd
# df = pd.read_csv("nato_phonetic_alphabet.csv")
# letter_code_dict = dict(zip(df["letter"].to_list(), df["code"].to_list()))
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user = input("Enter your name: ")
# print([letter_code_dict[letter.upper()] for letter in user if letter.upper() in letter_code_dict])

#TODO 1. Create a dictionary in this format:
import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for(index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter your name: ").upper()
# print([row.code for (index, row) in df.iterrows() if row.letter in user.upper()])
print([dict[letter] for letter in user])