import RPi.GPIO as GPIO


class Motor(object):
    def __init__(self, forwards_pin, backwards_pin):
        self.forwards_pin = forwards_pin
        self.backwards_pin = backwards_pin
        self._setup_motor()

    @staticmethod
    def set_pin_state(pin, state):
        GPIO.output(pin, state)

    def _setup_motor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)
        GPIO.setup(self.forwards_pin, GPIO.OUT)
        GPIO.setup(self.backwards_pin, GPIO.OUT)

    def go_forwards(self):
        self.set_pin_state(self.forwards_pin, 1)

    def go_backwards(self):
        self.set_pin_state(self.backwards_pin, 1)

    def stop(self):
        self.set_pin_state(self.forwards_pin, 0)
        self.set_pin_state(self.backwards_pin, 0)

    @staticmethod
    def _stop_motor():
        GPIO.cleanup()
