#TODO: Create a letter using starting_letter.txt

# #for each name in invited_names.txt
# name_list = []
# with open("./Input/Names/invited_names.txt") as names:
#     for name_ in names.readlines():
#         name = name_.strip("\n")  # name_.strip("")
#         name_list.append(name)
#
# #Replace the [name] placeholder with the actual name.
# letter_list = []
# with open("./Input/Letters/starting_letter.txt") as file:
#     content = file.read()
#     for name in name_list:
#         letter = content.replace("[name]", name)
#         letter_list.append(letter)
#
# #Save the letters in the folder "ReadyToSend".
# for name, letter in zip(name_list, letter_list):
#     with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as file:
#         file.write(letter)
#
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # 리스트 반환

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
