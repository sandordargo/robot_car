from robot import motors

motors.setup_motors()
motors.stop_motors()

motors.go_forwards(1)
motors.turn_right_forward(0.5)
motors.go_forwards(1)
motors.turn_right_forward(0.5)
motors.go_forwards(1)
motors.turn_right_forward(0.5)
motors.go_forwards(1)
motors.turn_right_forward(0.5)


# Reset the GPIO pins (turns off motors too)
motors.cleanup()
