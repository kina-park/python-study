# with open("letter_templates/letter_2.txt", 'r') as fr:
#     lines = fr.read()
# # print(lines)
# lines = lines.replace('[NAME]', 'hi')
# print(lines)
#
#
# # def customize_letter(new_str, file_path="letter_templates/letter_2.txt", old_str="[NAME]"):
# #     with open(file_path, 'r') as fr:
# #         lines = fr.readlines()
# #     replace(old_str, new_str)
# #     lines[0].split(" ")[1] = f"{new_str},\n"
# #     print(lines)
# #
# # customize_letter(new_str="kina,\n")
import pandas as pd
df = pd.read_csv("birthdays.csv")
birthdays_dict = {(df_row.month, df_row.day): df_row for (index, df_row) in df.iterrows()}
# print(birthdays_dict)

print(df.iterrows())
