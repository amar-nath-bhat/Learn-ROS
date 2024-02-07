#!/usr/bin/env python3

import math
import rospy, sys
from geometry_msgs.msg import Twist
import time


def move_turtle():
    rospy.init_node('circle_turtlebot', anonymous=True)
    velocity_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    msg = Twist()
    linear_speed = float(sys.argv[1])
    radius = float(sys.argv[2])
    duration = (2*math.pi*radius)/linear_speed
    initial_time = time.time()
    msg.linear.x = linear_speed

    angular_speed = linear_speed / radius
    msg.angular.z = angular_speed
    
    # print(initial_time)
    while time.time() - initial_time < duration:
        velocity_pub.publish(msg)
        rate.sleep()
    # print(time.time())
    # print(duration)

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
