import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# 나의 풀이
# word = input("Enter a word: ").upper()
# is_on = True
# while is_on:
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         word = input("Enter a word: ").upper()
#     else:
#         output_list = [phonetic_dict[letter] for letter in word]
#         is_on = False
# print(output_list)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic() # 여기서 자기 자신 호출 다시 시작!
    else:
        print(output_list)

generate_phonetic()
