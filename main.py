def on_button_pressed_a2():
    basic.show_arrow(ArrowNames.NORTH, 500)
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a2)

def on_button_pressed_b2():
    input.acceleration(Dimension.X)
    basic.show_number(Dimension.X)
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b2)
