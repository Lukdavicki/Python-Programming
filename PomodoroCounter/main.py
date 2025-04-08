from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label_timer.config(text ="Timer", fg=RED)
    label_checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label_timer.config(text="BREAK", fg=PINK)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_timer.config(text="BREAK", fg=RED)
    else:
        countdown(work_sec)
        label_timer.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_count()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += CHECKMARK
            label_checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(padx=50, pady=50, bg=YELLOW)
# timer label
label_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)
# canvas
canvas = Canvas(width=350, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(175, 112, image=tomato_img)
timer_text = canvas.create_text(175, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)
# start btn
button_start = Button(text="Start", borderwidth=0, bg=YELLOW, command=start_count)
button_start.grid(column=0, row=2)
# reset btn
button_reset = Button(text="Reset", borderwidth=0, bg=YELLOW, command=reset_timer)
button_reset.grid(column=2, row=2)
# checkmark label
label_checkmark = Label(fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)

window.mainloop()
