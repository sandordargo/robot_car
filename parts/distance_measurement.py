import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class DistanceDetector(object):

    def __init__(self):
        self.pinTrigger = 17
        self.pinEcho = 18
        print("Ultrasonic Measurement")

        GPIO.setup(self.pinTrigger, GPIO.OUT)
        GPIO.setup(self.pinEcho, GPIO.IN)

    def detect_distance(self):
        enter_time = time.time()
        GPIO.output(self.pinTrigger, False)
        time.sleep(0.1)
        GPIO.output(self.pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.pinTrigger, False)
        start_time = time.time()
        while GPIO.input(self.pinEcho) == 0:
            start_time = time.time()

        while GPIO.input(self.pinEcho) == 1:
            stop_time = time.time()
            if stop_time-start_time >= 0.04:
                print("Hold on there! You're too close for me to see.")
                stop_time = start_time
                break

        elapsed_time = stop_time - start_time
        distance = elapsed_time * 34326
        distance /= 2
        print("Distance : %.1f" % distance)
        measurement_time = time.time() - enter_time
        print("Measurement time: {}".format(measurement_time))
        return distance, measurement_time


if __name__ == "__main__":
    detector = DistanceDetector()
    try:
        while True:
            detector.detect_distance()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup
