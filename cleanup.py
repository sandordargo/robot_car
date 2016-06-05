import RPi.GPIO as GPIO

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    for num in range(1,41):
        GPIO.setup(num, GPIO.OUT)
        GPIO.output(num, False)
    GPIO.cleanup()
