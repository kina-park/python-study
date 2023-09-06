from tkinter import *
import random
import pandas as pd

current_card = {}
BACKGROUND_COLOR = "#B1DDC6"
# -------------------------------- 데이터 불러오기 -----------------------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def is_known():
    to_learn.remove(current_card) # 데이터 삭제하고
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card() # 이 함수 그대로

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) # 여기서 취소하고
    current_card = random.choice(to_learn)
    french = current_card["French"]
    canvas.itemconfig(image_canvas, image=card_front_image_path)
    canvas.itemconfig(title_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text=french, fill="black")
    flip_timer = window.after(3000, func=flip_card) # 그 다음부터 반복

def flip_card():
    english = current_card["English"]
    canvas.itemconfig(image_canvas, image=card_back_image_path)
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=english, fill="white")

# -------------------------------- UI 만들기 --------------------------------
# window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# canvas
card_front_image_path = PhotoImage(file="images/card_front.png")
card_back_image_path = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
image_canvas = canvas.create_image(400, 263, image=card_front_image_path)
title_canvas = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word_canvas = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# button
right_image_path = PhotoImage(file="images/right.png")
wrong_image_path = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image_path, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_image_path, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()