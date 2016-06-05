from __future__ import print_function

import time
import motor
import distance_measurement
import sys


class RobotController(object):
    def __init__(self):
        right_motor_forwards_pin = 10
        right_motor_backwards_pin = 9
        left_motor_forwards_pin = 7
        left_motor_backwards_pin = 8
        self.left_motor = motor.Motor(left_motor_forwards_pin, left_motor_backwards_pin, 'left')
        self.right_motor = motor.Motor(right_motor_forwards_pin, right_motor_backwards_pin, 'right')
        self.distance_detector = distance_measurement.DistanceDetector()

    def keep_moving(self, duration_in_seconds=0):
        """
        Keeps the set direction for the given amount of seconds
        """
        step_time_in_second = 0.05
        print("Keep doing last action for {} seconds.".format(duration_in_seconds))
        remaining_duration = float(duration_in_seconds)
        while remaining_duration > 0.0:
            time.sleep(remaining_duration)
            remaining_duration -= step_time_in_second
            print("Time to go: {}".format(remaining_duration))
            distance_from_obstacle = self.distance_detector.detect_distance()
            if distance_from_obstacle < 20:
                self.stop_motors()
                print("Obstacle is too close: {}. Stopping robot, waiting for next command".
                      format(distance_from_obstacle))
                # GPIO.cleanup
                # sys.exit()
                return

    def go_forwards(self, duration_in_seconds=0):
        """
        Turn both motors forwards
        """
        print("Move both motor forwards")
        self.right_motor.go_forwards()
        self.left_motor.go_forwards()
        self.keep_moving(duration_in_seconds)

    def stop_motors(self):
        """
        Stop both motors
        """
        print("Stop both motors")
        self.left_motor.stop()
        self.right_motor.stop()

    def go_backwards(self, duration_in_seconds=0):
        """
        Turn both motors backwards
        """
        print("Move both motor backwards")
        self.right_motor.go_backwards()
        self.left_motor.go_backwards()
        self.keep_moving(duration_in_seconds)

    def turn_left_forward(self, duration_in_seconds=0):
        """
        Turn left by moving right wheel forwards and left backwards
        """
        print("Turn left forwards")
        self.right_motor.go_forwards()
        self.left_motor.go_backwards()
        self.keep_moving(duration_in_seconds)

    def turn_right_forward(self, duration_in_seconds=0):
        """
        Turn right by moving left wheel forwards and right backwards
        """
        print("Turn right forwards")
        self.left_motor.go_forwards()
        self.right_motor.go_backwards()
        self.keep_moving(duration_in_seconds)

    def turn_slight_left_forward(self, duration_in_seconds=0):
        """
        Turn left by moving right wheel forwards and stop left
        """
        print("Turn slight left forwards")
        self.right_motor.go_forwards()
        self.left_motor.stop()
        self.keep_moving(duration_in_seconds)

    def turn_slight_right_forward(self, duration_in_seconds=0):
        """
        Turn right by moving left wheel forwards and stop right
        """
        print("Turn slight right forwards")
        self.left_motor.go_forwards()
        self.right_motor.stop()
        self.keep_moving(duration_in_seconds)

    def turn_left_backward(self, duration_in_seconds=0):
        """
        Turn left by moving right wheel backwards and left forwards
        """
        print("Turn left backwards")
        self.right_motor.go_backwards()
        self.left_motor.go_forwards()
        self.keep_moving(duration_in_seconds)

    def turn_right_backward(self, duration_in_seconds=0):
        """
        Turn right by moving left wheel backwards and right forwards
        """
        print("Turn right backwards")
        self.left_motor.go_backwards()
        self.right_motor.go_forwards()
        self.keep_moving(duration_in_seconds)

    def turn_slight_left_backward(self, duration_in_seconds=0):
        """
        Turn left by moving right wheel backwards and stop left
        """
        print("Turn slight left forwards")
        self.right_motor.go_backwards()
        self.left_motor.stop()
        self.keep_moving(duration_in_seconds)

    def turn_slight_right_backward(self, duration_in_seconds=0):
        """
        Turn right by moving left wheel backwards and stop right
        """
        print("Turn slight right forwards")
        self.left_motor.go_backwards()
        self.right_motor.stop()
        self.keep_moving(duration_in_seconds)

    def stop_robot(self):
        self.left_motor._stop_motor()
        self.right_motor._stop_motor()

