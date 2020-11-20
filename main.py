radio.set_group(125)
basic.show_string("Z SENDER")
input.set_accelerometer_range(AcceleratorRange.EIGHT_G)

def on_forever():
    radio.send_number(input.acceleration(Dimension.Z))
basic.forever(on_forever)





 



"""
def on_button_pressed_a2():
    radio.send_string("YES")
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a2)

def on_button_pressed_b2():
    radio.send_string("NO")
    basic.pause(200)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b2)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)
"""