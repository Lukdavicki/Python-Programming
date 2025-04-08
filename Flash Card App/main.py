from tkinter import *

import pandas
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
timer = None
current_card = None

window = Tk()
window.title("Flash Card Converter")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# If block for checking csv existance

if os.path.isfile("data/words_to_learn.csv"):
    data = pd.read_csv("data/words_to_learn.csv")
else:
    data = pd.read_csv("data/french_words.csv")


to_learn_dict = data.to_dict(orient="records")

canvas_back_img = PhotoImage(file="images/card_back.png")
canvas_front_img = PhotoImage(file="images/card_front.png")




def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    canvas.itemconfig(canvas_image, image=canvas_front_img)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_text, text=current_card["French"])
    window.after(3000, change_card)
def change_card():
    global current_card

    # window.after(3000,next_card)
    canvas.itemconfig(canvas_image, image=canvas_back_img)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_text, text=current_card["English"])

def is_known():
    to_learn_dict.remove(current_card)
    new_data = pandas.DataFrame(to_learn_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)

canvas_image = canvas.create_image(400, 263, image=canvas_front_img)
card_title = canvas.create_text(400, 150, fill="black", font=TITLE_FONT)
card_text = canvas.create_text(400, 263, fill="black", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

btn_image_false = PhotoImage(file="images/wrong.png")
btn_image_true = PhotoImage(file="images/right.png")

button_right = Button(image=btn_image_true, highlightthickness=0, border=0, command=is_known)
button_right.grid(row=1, column=0)

button_wrong = Button(image=btn_image_false, highlightthickness=0, border=0, command=next_card)
button_wrong.grid(row=1, column=1)

flip_timer = window.after(3000, change_card)
next_card()

window.mainloop()
