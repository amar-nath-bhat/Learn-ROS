#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt

class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.rate = rospy.Rate(10)  
        self.turtle_pose = Pose()

    def pose_callback(self, data):
        self.turtle_pose = data

    def move(self, linear_speed, angular_speed, duration):
        vel_msg = Twist()
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = angular_speed

        start_time = rospy.Time.now().to_sec()

        while (rospy.Time.now().to_sec() - start_time) < duration:
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def rotate_to_goal(self, goal_x, goal_y):
        goal_theta = atan2(goal_y - self.turtle_pose.y, goal_x - self.turtle_pose.x)

        while abs(self.turtle_pose.theta - goal_theta) > 0.01:
            self.move(0, 1, 0.1)

    def go_to_goal(self, goal_x, goal_y):
        distance = sqrt((goal_x - self.turtle_pose.x)**2 + (goal_y - self.turtle_pose.y)**2)

        while distance > 0.1:
            linear_speed = 1.5 * distance
            angular_speed = 4 * (atan2(goal_y - self.turtle_pose.y, goal_x - self.turtle_pose.x) - self.turtle_pose.theta)

            self.move(linear_speed, angular_speed, 0.1)

            distance = sqrt((goal_x - self.turtle_pose.x)**2 + (goal_y - self.turtle_pose.y)**2)

if __name__ == '__main__':
    try:
        controller = TurtleController()

        controller.move(1, 0, 3)
        controller.go_to_goal(9, 9)
        # controller.draw_D()
        controller.go_to_goal(2.5, 5.5)
        # controller.rotate_goal(3.14)
    except rospy.ROSInterruptException:
        pass
