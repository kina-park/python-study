from tkinter import *
import pandas as pd
import random

french_word = ""
DELETE = False
BACKGROUND_COLOR = "#B1DDC6"
# -------------------------------- 데이터 불러오기 -----------------------------------
df = pd.read_csv("data/french_words.csv")
french = df["French"].tolist()
english = df["English"].tolist()
french_english = dict(zip(french, english))
# -------------------------------- 타이머 -----------------------------------
def timer(number):
    global french_word
    window.after(1000, timer, number+1)
    if (number % 3 == 0) & (number % 2 == 0):
         front()
    elif (number % 3 == 0) & (number % 2 == 1):
        back(french_word)
    else:
        pass

def front():
    card_image.itemconfig(image_container, image=card_front_image_path)
    language_label.config(text="French", background="white")
    global french_word
    french_word = random.choice(french)
    word_label.config(text=french_word, background="white")

def back(f_word):
    global french_word
    card_image.itemconfig(image_container, image=card_back_image_path)
    language_label.config(text="English", background=BACKGROUND_COLOR)
    english_word = french_english[french_word]
    word_label.config(text=english_word, background=BACKGROUND_COLOR)
    if DELETE:
        del french_english[french_word]
    else:
        pass

# -------------------------------- button 누르면 --------------------------------
def right_click():
    global DELETE
    DELETE = True

def wrong_click():
    global DELETE
    DELETE = False
# -------------------------------- UI 만들기 --------------------------------
# window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas, label
card_front_image_path = PhotoImage(file="images/card_front.png")
card_back_image_path = PhotoImage(file="images/card_back.png")

card_image = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image_container = card_image.create_image([400, 263], image=card_front_image_path)
card_image.grid(column=0, row=0, columnspan=2)

language_label = Label(window, font=("Arial", 40, "italic"), background="white")
language_label.place(x=300, y=150)

word_label = Label(window, font=("Arial", 60, "bold"), background="white")
word_label.place(x=300, y=263)

# button
right_image_path = PhotoImage(file="images/right.png")
wrong_image_path = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image_path, highlightthickness=0, command=right_click)
wrong_button = Button(image=wrong_image_path, highlightthickness=0, command=wrong_click)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

timer(0)

window.mainloop()
