#!/usr/bin/env python3

import rospy
from robot_pkg.msg import Message

def publisher():
    pub = rospy.Publisher('chatter', Message, queue_size=10)
    rospy.init_node('talker')
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        rospy.loginfo("Data Published")
        msg = Message()
        msg.message = "Custom Message Generated !"
        msg.number1 = 10
        msg.number2 = 1.3
        msg.decision = True
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass