from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=800, height=600)
window.config(padx=50,pady=50)
window.config(bg="grey")
# Label
my_label = Label(text="I am a label")
my_label.grid(column=0, row=0)


# button
# window.counter = 0
# TO ADD A VARIABLE ACCESSIBLE IN THE OUTER SCOPE IT HAS TO BE ADDED TO THE Tk() CLASS WITH THE DOT NOTATION
def change_label():
    my_label.config(text=input.get())


# window.counter += 1
# my_label["text"] = window.counter
# if window.counter == 10 :
#     new_label = Label(text="You have hit 10 clicks!")
#     new_label.pack()

button = Button(text="Click me 2!", command=change_label)
button.grid(column=2, row=0)
button = Button(text="Click me!", command=change_label)
button.grid(column=1, row=1)


# Entry
input = Entry()
input.grid(column=3, row=2)

window.mainloop()
