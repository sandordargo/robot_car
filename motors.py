import RPi.GPIO as GPIO
import time

right_motor_forwards_pin = 9
right_motor_backwards_pin = 10

left_motor_forwards_pin = 8
left_motor_backwards_pin = 7


def setup_motors():
    # Set the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)
    # Set the GPIO Pin mode
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)    


def keep_moving(duration_in_seconds=0):
    '''
    Keeps the set direction for the given amount of seconds
    '''
    time.sleep(duration_in_seconds)    


def right_forwards(duration_in_seconds=0):
    '''
    Turn the right motor forwards
    '''
    right_motor_forwards_pin(1)
    right_motor_backwards_pin(0)
    keep_moving(duration_in_seconds)


def left_forwards(duration_in_seconds=0):
    '''
    Turn the left motor forwards
    '''
    left_motor_backwards_pin(0)
    left_motor_forwards_pin(1)
    keep_moving(duration_in_seconds)


def go_forwards(duration_in_seconds=0):
    '''
    Turn both motors forwards
    '''
    right_forwards()
    left_forwards()
    keep_moving(duration_in_seconds)


def left_stop(duration_in_seconds=0):
    '''
    Stop the left motor
    '''
    left_motor_backwards_pin(0)
    left_motor_forwards_pin(0)
    keep_moving(duration_in_seconds)


def right_stop(duration_in_seconds=0):
    '''
    Stop the right motor
    '''
    right_motor_forwards_pin(0)
    right_motor_backwards_pin(0) 
    keep_moving(duration_in_seconds)


def stop_motors():
    '''
    Stop both motors
    '''
    right_stop()
    left_stop()


def left_backwards(duration_in_seconds=0):
    '''
    Turn the left motor backwards
    '''
    left_motor_backwards_pin(1)
    left_motor_forwards_pin(0)
    keep_moving(duration_in_seconds)


def right_backwards(duration_in_seconds=0):
    '''
    Turn the right motor backwards
    '''
    right_motor_forwards_pin(0)
    right_motor_backwards_pin(1)
    keep_moving(duration_in_seconds)


def go_backwards(duration_in_seconds=0):
    '''
    Turn both motors backwards
    '''
    right_backwards()
    left_backwards()
    keep_moving(duration_in_seconds)


def turn_left_forward(duration_in_seconds=0):
    '''
    Turn left by moving right wheel forwards and left backwards
    '''
    right_forwards()
    left_backwards()
    keep_moving(duration_in_seconds)


def turn_right_forward(duration_in_seconds=0):
    '''
    Turn right by moving left wheel forwards and right backwards
    '''
    left_forwards()
    right_backwards()
    keep_moving(duration_in_seconds)


setup_motors()
# Turn all motors off
stop_motors()
go_forwards(1)
turn_right_forward(0.5)
go_forwards(1)
turn_right_forward(0.5)
go_forwards(1)
turn_right_forward(0.5)


# Reset the GPIO pins (turns off motors too)
GPIO.cleanup()
