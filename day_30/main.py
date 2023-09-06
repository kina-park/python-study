# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary{"non_existent_key"}

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text+5)

# Catching Exceptions
# try: 예외를 유발할 수 있는 뭔가를 실행하는 코드 블록
# except: 만약에 예외가 있었다면 실행하는 코드 블록
# else: 예외가 없었을 때 시행하는 코드 블록
# finally: 어떤 일이 일어나도 시행되어야 할 코드 블록

# try:
#     file = open("a_file.txt")
#     # 여기 코드 실행했는데 오류나면
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["non_existent_key"]) # 해당 라인 실패, 예외 생성
# except FileNotFoundError: # 예외 잡기
#     # 여기서 실행되도록
#     file = open("a_file.txt", "w")
#     file.write("Hello World")
# except KeyError as error_message: # 예외 잡기
#     print(f"The key {error_message} does not exist.")
# else:
#     # what else do you want to do?
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise TypeError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))
bmi = weight / height ** 2

if height > 3 :
    raise ValueError("Human height should not be over 3 meters.")





