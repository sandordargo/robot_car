from __future__ import print_function

import robot_controller

import argparse
import random
import time


def parse_arguments():
    parser_description = \
        """
        Self-driver script for my rPi robot.
        """

    parser = argparse.ArgumentParser(description=parser_description)
    parser.add_argument('-t', '--drive_time',
                        dest='drive_time',
                        type=float,
                        default=10.0,
                        help='The time while the self-driver should be turned on')

    return parser.parse_args()


def self_drive(drive_time=10.0):
    my_robot = robot_controller.RobotController()
    default_step_time = 1.0
    default_turn_time = 0.2

    movements_list_without_forward = [my_robot.go_backwards, my_robot.turn_left_backward, my_robot.turn_left_forward,
                                      my_robot.turn_right_backward, my_robot.turn_right_forward,
                                      my_robot.turn_slight_left_backward, my_robot.turn_slight_left_forward,
                                      my_robot.turn_slight_right_backward, my_robot.turn_slight_right_forward]

    movements_list_with_forward = [my_robot.go_backwards, my_robot.turn_left_backward, my_robot.turn_left_forward,
                                      my_robot.turn_right_backward, my_robot.turn_right_forward, my_robot.go_forwards,
                                      my_robot.turn_slight_left_backward, my_robot.turn_slight_left_forward,
                                      my_robot.turn_slight_right_backward, my_robot.turn_slight_right_forward]
    try:
        my_robot.stop_motors()

        start_time = time.time()

        my_robot.go_forwards(default_step_time)

        last_movement_time = time.time() - start_time
        elapsed_time = last_movement_time
        while elapsed_time < drive_time:
            if abs(last_movement_time - default_step_time) < 0.1:
                step_start_time = time.time()
                random.choice(movements_list_with_forward)(default_turn_time)
                last_movement_time = time.time() - step_start_time
            else:
                step_start_time = time.time()
                random.choice(movements_list_without_forward)(default_turn_time)
                last_movement_time = time.time() - step_start_time
            elapsed_time += last_movement_time
    finally:
        my_robot.stop_robot()

if __name__ == "__main__":
    arguments = parse_arguments()
    self_drive(arguments.drive_time)


