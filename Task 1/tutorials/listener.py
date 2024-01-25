#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

def num_cb(data):
    print("Data: ",data)
     
def listener():
    rospy.init_node('int_subscriber', anonymous=True)

    rospy.Subscriber("number_out", Int16, num_cb)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()