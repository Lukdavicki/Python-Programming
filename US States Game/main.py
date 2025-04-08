import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.setup(725,491)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states =[]

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct","What's another states name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        # changed the standard int(state_data.x) to int(state_data.x.iloc[0]) so FUTURE Pandas won't give an error
        t.write(answer_state)

difference = list(set(all_states).symmetric_difference(set(guessed_states)))
print(difference)
state_learn_df = pandas.DataFrame(difference)
state_learn_df.to_csv("states_to_learn.csv")
