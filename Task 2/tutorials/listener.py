#!/usr/bin/env python3
import rospy
from robot_pkg.msg import Message

def callback(data):
    print(f"Message: {data.message} Number1: {data.number1} Number2: {data.number2} Decision: {data.decision}")
     
def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", Message, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()