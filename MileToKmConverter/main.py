from tkinter import *

# Window Config
window = Tk()
window.title("Mile To Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

KM_MULTIPLIER = 1.609


# window.config(bg="grey")

# Function

def calculate():
    user_input = input.get()
    if user_input.isdigit():
        km = float(user_input) * KM_MULTIPLIER
        result_label.config(text=km)


# Elements

input = Entry()
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
