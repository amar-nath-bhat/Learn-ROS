#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt
import curses

class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)

        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.rate = rospy.Rate(10)
        self.turtle_pose = Pose()

        self.stdscr = curses.initscr()
        curses.cbreak()
        self.stdscr.keypad(True)

    def pose_callback(self, data):
        self.turtle_pose = data

    def move(self, linear_speed, angular_speed):
        vel_msg = Twist()
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = angular_speed
        self.velocity_publisher.publish(vel_msg)

    def stop(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def control_turtle(self):
        while True:
            key = self.stdscr.getch()

            if key == ord('q'):
                break
            elif key == curses.KEY_UP:
                self.move(1, 0)
            elif key == curses.KEY_DOWN:
                self.move(-1, 0)
            elif key == curses.KEY_LEFT:
                self.move(0, 1)
            elif key == curses.KEY_RIGHT:
                self.move(0, -1)

            self.rate.sleep()

        # Stop the turtle when the loop is exited
        self.stop()

    def run(self):
        try:
            self.control_turtle()
        finally:
            curses.endwin()

if __name__ == '__main__':
    try:
        controller = TurtleController()
        controller.run()

    except rospy.ROSInterruptException:
        pass