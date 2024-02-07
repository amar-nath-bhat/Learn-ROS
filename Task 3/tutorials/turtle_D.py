#!/usr/bin/env python3

from cmath import sqrt
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleController:
    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(1)
        self.linear_x = 0.5
        self.radius = 1
        self.angle = self.linear_x/self.radius
        self.duration = (math.pi * self.radius)/self.linear_x

    def make_D(self):
        msg = Twist()
        start_time = rospy.Time.now().to_sec()

        while rospy.Time.now().to_sec() - start_time <= self.duration:
            msg.linear.x = self.linear_x
            msg.angular.z = self.angle
            self.velocity_publisher.publish(msg)
        
        self.stop()

        start_time = rospy.Time.now().to_sec()
        while rospy.Time.now().to_sec() - start_time <= 1:
            msg.linear.x = 0
            msg.angular.z = math.pi/2
            self.velocity_publisher.publish(msg)

        self.stop()

        start_time = rospy.Time.now().to_sec()
        self.duration = 2 / self.angle
        while rospy.Time.now().to_sec() - start_time <= self.duration:
            msg.linear.x = self.linear_x
            msg.angular.z = 0
            self.velocity_publisher.publish(msg)

        self.stop()    

    def stop(self):
        vel_msg = Twist()
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        controller = TurtleController()
        controller.make_D()

    except rospy.ROSInterruptException:
        pass
