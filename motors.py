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


def right_forwards():
    '''
    Turn the right motor forwards
    '''
    right_motor_forwards_pin(1)
    right_motor_backwards_pin(0)


def left_forwards():
    '''
    Turn the left motor forwards
    '''
    left_motor_backwards_pin(0)
    left_motor_forwards_pin(1)

def go_forwards():
    '''
    Turn both motors forwards
    '''
    right_forwards()
    left_forwards()


def left_stop():
    '''
    Stop the left motor
    '''
    left_motor_backwards_pin(0)
    left_motor_forwards_pin(0)


def right_stop():
    '''
    Stop the right motor
    '''
    right_motor_forwards_pin(0)
    right_motor_backwards_pin(0) 


def stop_motors():
    '''
    Stop both motors
    '''
    right_stop()
    left_stop()


def left_backwards():
    '''
    Turn the left motor backwards
    '''
    left_motor_backwards_pin(1)
    left_motor_forwards_pin(0)


def right_backwards():
    '''
    Turn the right motor backwards
    '''
    right_motor_forwards_pin(0)
    right_motor_backwards_pin(1)


def go_backwards():
    '''
    Turn both motors backwards
    '''
    right_backwards()
    left_backwards()

def turn_left_forward():
    '''
    Turn left by moving right wheel forwards and left backwards
    '''
    right_forwards()
    left_backwards()

def turn_right_forward():
    '''
    Turn right by moving left wheel forwards and right backwards
    '''
    left_forwards()
    right_backwards()


setup_motors()
# Turn all motors off
stop_motors()
go_forwards()
# Wait for 1 second
time.sleep(1)
turn_right_forward()
time.sleep(0.5)
go_forwards()
# Wait for 1 second
time.sleep(1)
turn_right_forward()
time.sleep(0.5)
go_forwards()
# Wait for 1 second
time.sleep(1)
turn_right_forward()
time.sleep(0.5)


# Reset the GPIO pins (turns off motors too)
GPIO.cleanup()
