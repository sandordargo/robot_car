from parts import robot_controller

my_robot = robot_controller.RobotController()

my_robot.stop_motors()

my_robot.go_forwards(1)
my_robot.turn_right_forward(0.5)
my_robot.go_forwards(1)
my_robot.turn_right_forward(0.5)
my_robot.go_forwards(1)
my_robot.turn_right_forward(0.5)
my_robot.go_forwards(1)
my_robot.turn_right_forward(0.5)

my_robot.stop_robot()


