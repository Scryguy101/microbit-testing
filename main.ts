input.onButtonPressed(Button.A, function on_button_pressed_a2() {
    basic.showArrow(ArrowNames.North, 500)
    basic.pause(200)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b2() {
    input.acceleration(Dimension.X)
    basic.showNumber(Dimension.X)
    basic.pause(200)
    basic.clearScreen()
})
