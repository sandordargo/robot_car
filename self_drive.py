from __future__ import print_function

import argparse
import random
import time

from parts import robot_controller


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


def weighted_choice(weights):
    totals = []
    running_total = 0

    for weight in weights:
        running_total += weight
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i


def self_drive(drive_time=10.0):
    my_robot = robot_controller.RobotController()
    default_step_time = 1.0
    default_turn_time = 0.2

    movements_list_without_forward = [(my_robot.go_backwards, 1), (my_robot.turn_left_backward, 1),
                                      (my_robot.turn_left_forward, 1), (my_robot.turn_right_backward, 1),
                                      (my_robot.turn_right_forward, 1), (my_robot.turn_slight_left_backward, 1),
                                      (my_robot.turn_slight_left_forward, 1), (my_robot.turn_slight_right_backward, 1),
                                      (my_robot.turn_slight_right_forward, 1)]

    movements_list_with_forward = [(my_robot.go_backwards, 1), (my_robot.turn_left_backward, 1),
                                   (my_robot.turn_left_forward, 1), (my_robot.turn_right_backward, 1),
                                   (my_robot.turn_right_forward, 1), (my_robot.turn_slight_left_backward, 1),
                                   (my_robot.turn_slight_left_forward, 1), (my_robot.turn_slight_right_backward, 1),
                                   (my_robot.turn_slight_right_forward, 1), (my_robot.go_forwards, 8)]
    try:
        my_robot.stop_motors()

        start_time = time.time()

        my_robot.go_forwards(default_step_time)

        last_movement_time = time.time() - start_time
        elapsed_time = last_movement_time
        while elapsed_time < drive_time:
            if abs(last_movement_time - default_step_time) < 0.1:
                step_start_time = time.time()
                movements_list_with_forward[weighted_choice([x[1] for x in movements_list_with_forward])][0](
                    default_turn_time)
                last_movement_time = time.time() - step_start_time
            else:
                step_start_time = time.time()
                movements_list_without_forward[weighted_choice([x[1] for x in movements_list_without_forward])][0](
                    default_turn_time)
                last_movement_time = time.time() - step_start_time
            elapsed_time += last_movement_time
    finally:
        my_robot.stop_robot()


if __name__ == "__main__":
    arguments = parse_arguments()
    self_drive(arguments.drive_time)
