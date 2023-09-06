from tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # 여백 추가 padding 

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(column=0, row=0) # 레이아웃 방법 중 하나. pack과 같은 프로그램에서 사용될 수 없음

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()

