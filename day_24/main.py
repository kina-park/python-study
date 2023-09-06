# 절대 경로
# file = open("/Users/kina/Desktop/my_file.txt") # Root 디렉토리는  c드라이브
# contents = file.read()
# print(contents)
# file.close()

# 상대 경로
file = open("../../../Desktop/my_file.txt") # Root 디렉토리는  c드라이브
contents = file.read()
print(contents)
file.close()

# "C:\Users\kina\PycharmProjects\udemy\day_24\main.py"
# "C:\Users\kina\Desktop\my_file.txt"

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents) # 해당 라인 실행 후 , 자동으로 파일을 닫음

# with open("my_file.txt", mode="w") as file: # 쓰기 모드
#     file.write("\nNew text.")
#
#
# with open("my_file.txt", mode="a") as file: # 이어쓰기 모드
#     file.write("\nNew text.")

# with open("my_file_2.txt", mode="w") as file:  # 쓰기 모드
#     file.write("New text.")



