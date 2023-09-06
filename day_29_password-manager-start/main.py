from tkinter import *  # 모든 클래스와 상수를 임포트
from tkinter import messagebox # messagebox는 모듈
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password) # 바로 클립보드에 복사됨
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_input.get()
    user_email = email_input.get()
    user_password = password_input.get()

    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=user_website,
            message=f"These are the details entered: \nEmail: {user_email} \nPassword: {user_password} \nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a+") as file:
                file.write(f"{user_website} | {user_email} | {user_password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus_set()
# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# label
website_lab = Label(text="Website:", bg="white")
website_lab.grid(column=0, row=1)
email_lab = Label(text="Email/Username:", bg="white")
email_lab.grid(column=0, row=2)
password_lab = Label(text="Password:", bg="white")
password_lab.grid(column=0, row=3, sticky="news")

# Entry
website_input = Entry(width=35, highlightcolor="#00BFFF", highlightthickness=1)
website_input.grid(sticky=E+W, column=1, row=1, columnspan=2)
website_input.focus_set()
# user_website = website_input.get()

email_input = Entry(width=35, highlightcolor="#00BFFF", highlightthickness=1)
email_input.grid(sticky=E+W, column=1, row=2, columnspan=2)
email_input.insert(0, "qkrrlsk8062@naver.com")
# user_email = email_input.get()

password_input = Entry(width=27, highlightcolor="#00BFFF", highlightthickness=1)
password_input.grid(sticky=W+S, column=1, row=3)
# user_password = password_input.get()

# button
gen_button = Button(text="Generate Password", bg="white", command=generate_password)
gen_button.grid(sticky=W+E, column=2, row=3)
add_button = Button(text="Add", width=36, bg="white", command=save)
add_button.grid(sticky=E+W, column=1, row=4, columnspan=2)

window.mainloop()