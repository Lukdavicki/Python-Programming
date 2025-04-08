import pytube
import os
from moviepy.editor import *
from tkinter import *

# pytube.innertube._cache_dir = os.path.join(os.getcwd(), "cache")
# pytube.innertube._token_file = os.path.join(pytube.innertube._cache_dir, 'tokens.json')
print("Python Code Starting")
# VIDEO_SAVE_DIRECTORY = "./video"
AUDIO_SAVE_DIRECTORY = "./audio"
BACKGROUND_RED = "#E63946"
ACCENT_WHITE = "#F1FAEE"
yt = None


def get_entry():
    global yt
    yt = pytube.YouTube(link_input.get())
    canvas.itemconfig(title_text, text=yt.title)


def download():
    yd = yt.streams.get_highest_resolution()
    video = yd.download(AUDIO_SAVE_DIRECTORY)
    print(video)
    final_video = video.removesuffix(".mp4")
    if os.path.exists(video):
        video_to_audio = VideoFileClip(video)
        video_to_audio.audio.write_audiofile(f"{final_video}.mp3")
        if os.path.exists(f"{final_video}.mp3"):
            link_input.delete(0, END)
            canvas.itemconfig(title_text, text="Pobrane!")


window = Tk()
window.title("Jutubowy Pobieracz 1.0")
#
#
logo_image = PhotoImage(file="img/logo.png")
canvas = Canvas(width=600, height=400, highlightthickness=0, bg=BACKGROUND_RED)
canvas_image = canvas.create_image(540, 70, image=logo_image)
canvas.grid(row=0, column=0, columnspan=2, rowspan=4)

title_label = Label(padx=30, text="Jutubowy Pobieracz", font=("Quicksand", 30, "bold"), bg=BACKGROUND_RED,
                    fg=ACCENT_WHITE)
title_label.grid(row=0, column=0, columnspan=1)
#
#
link_input = Entry(window)
link_input.config(background=ACCENT_WHITE, borderwidth=1, width=65)
link_input.grid(row=1, column=0)
#
#
search_button = Button(text="Szukaj!", background=BACKGROUND_RED, fg=ACCENT_WHITE, font=("Quicksand", 15, "bold"),
                       command=get_entry)
search_button.grid(row=1, column=1)

title_text = canvas.create_text(300, 250, text="", fill=ACCENT_WHITE, font=("Quicksand", 12, "bold"))

download_button = Button(text="Sciągaj!", background=BACKGROUND_RED, fg=ACCENT_WHITE, font=("Quicksand", 15, "bold"),
                         command=download)
download_button.grid(row=3, column=0, columnspan=2)

window.mainloop()
