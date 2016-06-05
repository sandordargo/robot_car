import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinTrigger = 17
pinEcho = 18
print("Ultrasonic Measurement")

GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
try:
    while True:
        GPIO.output(pinTrigger, False)
        time.sleep(0.5)
        GPIO.output(pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)
        StartTime = time.time()
        while GPIO.input(pinEcho)==0:
            StartTime = time.time()

        while GPIO.input(pinEcho)==1:
            StopTime = time.time()
            if StopTime-StartTime >= 0.04:
                print("Hold on there! You're too close for me to see.")
                StopTime = StartTime
                break

        ElapsedTime = StopTime - StartTime
        Distance = ElapsedTime * 34326
        Distance = Distance / 2
        print("Distance : %.1f" % Distance)
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
