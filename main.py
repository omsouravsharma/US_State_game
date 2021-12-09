import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_state = data.state.to_list()
score = 0
user_guess = []

while len(user_guess) < 50:
    answer_state = screen.textinput(title=f"{len(user_guess)}/50 state correct",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in user_guess:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("learn_more.csv")

        break

    if answer_state in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
        user_guess.append(answer_state)



