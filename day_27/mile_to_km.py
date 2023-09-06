from tkinter import *

# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Entry
input = Entry(width=10, font=("Arial", 14, "bold"))
input.grid(column=1, row=0)

# Label
label1 = Label(text="Miles", font=("Arial", 14, "bold"))
label1.grid(column=2, row=0)

label2 = Label(text="is equal to", font=("Arial", 14, "bold"))
label2.grid(column=0, row=1)

label3 = Label(text="Km", font=("Arial", 14, "bold"))
label3.grid(column=2, row=1)

label4 = Label(text=0, font=("Arial", 14, "bold"))
label4.grid(column=1, row=1)


# Button
def button_clicked():
    input_mile = float(input.get())
    output_km = round(input_mile * 1.609, 3)
    label4.config(text=f"{output_km}")

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()