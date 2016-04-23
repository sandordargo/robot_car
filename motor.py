from __future__ import print_function

import RPi.GPIO as GPIO


class Motor(object):
    def __init__(self, forwards_pin, backwards_pin, name=None):
        self.forwards_pin = forwards_pin
        self.backwards_pin = backwards_pin
        self.name = name
        self._setup_motor()

    def set_pin_state(self, pin, state):
        GPIO.output(pin, state)

    @staticmethod
    def setup_gpio():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)

    def _setup_motor(self):
        GPIO.setup(self.forwards_pin, GPIO.OUT)
        GPIO.setup(self.backwards_pin, GPIO.OUT)
        print('setup {} motor'.format(self.name))

    def go_forwards(self):
        self.set_pin_state(self.backwards_pin, 0)
        self.set_pin_state(self.forwards_pin, 1)
        print('go forwards {} motor'.format(self.name))

    def go_backwards(self):
        self.set_pin_state(self.forwards_pin, 0)
        self.set_pin_state(self.backwards_pin, 1)
        print('go backwards {} motor'.format(self.name))

    def stop(self):
        self.set_pin_state(self.forwards_pin, 0)
        self.set_pin_state(self.backwards_pin, 0)
        print('stop {} motor'.format(self.name))

    @staticmethod
    def _stop_motor():
        GPIO.cleanup()
