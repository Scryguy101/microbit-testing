radio.setGroup(125)
input.onButtonPressed(Button.A, function on_button_pressed_a2() {
    radio.sendString("YES")
    basic.pause(200)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b2() {
    radio.sendString("NO")
    basic.pause(200)
    basic.clearScreen()
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
