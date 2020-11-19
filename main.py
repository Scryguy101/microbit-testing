def on_button_pressed_a2():
    basic.show_arrow(ArrowNames.NORTH)
input.on_button_pressed(Button.A, on_button_pressed_a2)

def on_button_pressed_b2():
    input.acceleration(Dimension.X)
input.on_button_pressed(Button.B, on_button_pressed_b2)
