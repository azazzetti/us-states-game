import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

is_on = True
correct_states = 0
guessed_states = []
states_to_learn = []

states = pd.read_csv("50_states.csv")

all_states = states.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        df = pd.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_row = states.loc[states["state"] == answer_state]
        x = float(state_row.x.iloc[0])
        y = float(state_row.y.iloc[0])
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(x, y)
        t.write(answer_state)
