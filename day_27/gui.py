import tkinter

window = tkinter.Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)  # 디폴트(최소) 사이즈

# Label (윈도우 안에 들어가는 컴포넌트)
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# my_label.place(x=0, y=0) # 왼쪽 맨 위 모서리에 배치
# my_label.pack()  # 화면에 레이블 컴포넌트를 자동으로 중앙에 배치
# my_label.pack(side="left")
# 아래와 인자 비교해보기
# import turtle
# tim = turtle.Turtle()
# tim.write()
my_label["text"] = "New text"
my_label.config(text="New text")

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked) # 함수를 호출하지 않고, 함수명만 사용하기 때문에 끝에 괄호 X
button.pack(side="left")

# Entry
input = tkinter.Entry(width=10)
input.pack(side="left")
print(input.get()) # 입력값을 문자열로 반환 -> 별 다른 결과를 주지 않음.


window.mainloop()  # 윈도우가 스크린에 계속 유지되도록  # 맨 마지막 코드

