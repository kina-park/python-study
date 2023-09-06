from tkinter import *  # 모든 클래스와 상수를 임포트
from tkinter import messagebox # messagebox는 모듈
import random
import pyperclip
import json
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
    new_user_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }
    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                #1. Reading old data
                data = json.load(file) # type(data): 파이썬의 dict 형식

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_user_data, file, indent=4)

        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as file:
                json.dump(new_user_data, file, indent=4)

        else:  # try 코드가 문제 없다면 트리거됨.
             # 2. Updating old data with new user data
            data.update(new_user_data)
            with open("data.json", "w") as file:
             # 3. Saving upated data
                json.dump(data, file, indent=4)

        finally: # 뭐가 됐든 무조건 실행
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus_set()

def find_password():
    user_website = website_input.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    # if, else로 할 수 있다면 if, else로 작성하기. 다른 쉬운 대안이 없을 때만 예외처리를 사용함. 
    if user_website in data:
        email = data[user_website]["email"]
        password = data[user_website]["password"]
    else:
        messagebox.showinfo(title="Error", message=f"No Details for {user_website} exists.")

    # try:
    #     with open("data.json", "r") as file:
    #         data = json.load(file)
    #         email = data[user_website]["email"]
    #         password = data[user_website]["password"]
    # except FileNotFoundError:
    #     messagebox.showinfo(title="Notice", message=f"No website {user_website}")
    # except json.decoder.JSONDecodeError:
    #     messagebox.showinfo(title="Notice", message=f"No website {user_website}")
    # except KeyError:
    #     messagebox.showinfo(title="Notice", message=f"No website {user_website}")
    # else:
    #     messagebox.showinfo(title="Notice", message=f"email: {email}\npassword: {password}")

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
website_input = Entry(width=27, highlightcolor="#00BFFF", highlightthickness=1)
website_input.grid(sticky=S+W, column=1, row=1, columnspan=2)
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
search_button = Button(text="Search", bg="white", command=find_password)
search_button.grid(sticky=W+E, column=2, row=1)


window.mainloop()