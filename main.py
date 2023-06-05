def on_button_pressed_a():
    global Num
    Num = Num + 2
    basic.show_number(Num)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Num
    Num = Num + 2
    basic.show_number(Num)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if Num >= 64:
        basic.show_icon(IconNames.DIAMOND)
    else:
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

Num = 0
Num = 2