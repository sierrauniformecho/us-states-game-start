import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's "
                                                                                             "name?").title()

    # exit code
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # check if input matches a state name (CamelCase und Low Case)
    # if yes, count States correct and show state name on map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        answer_data = data[data.state == answer_state]
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(float(answer_data.x), float(answer_data.y))
        state.write(answer_data.state.item())


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
