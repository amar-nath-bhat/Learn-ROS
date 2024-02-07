#!/usr/bin/env python3

from math import atan2, pi
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim_controller.srv import polygon, polygonResponse

class PolygonServer():
    def __init__(self):
        rospy.init_node('polygon_server', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.rate = rospy.Rate(10)  
        self.msg = Twist()
        self.turtle_pose = Pose()
        self.angle = 0  

        self.polygon_service = rospy.Service('draw_polygon', polygon, self.handle_polygon)

    def pose_callback(self, data):
        self.turtle_pose = data   

    def handle_polygon(self, req):
        angle = 2*pi/req.n
        duration = 0.5

        for _ in range(req.n):

            start_time = rospy.Time.now().to_sec()
            
            while rospy.Time.now().to_sec() - start_time <= duration:
                self.msg.angular.z = angle
                self.velocity_publisher.publish(self.msg)

            self.msg.angular.z = 0
            self.velocity_publisher.publish(self.msg)

            start_time = rospy.Time.now().to_sec()

            while rospy.Time.now().to_sec()-start_time<=duration:
                self.msg.linear.x = 2
                self.velocity_publisher.publish(self.msg)
            self.msg.linear.x = 0
            self.velocity_publisher.publish(self.msg)
        return polygonResponse()

if __name__ == '__main__':
    try:
        controller = PolygonServer()
        rospy.spin() 

    except rospy.ROSInterruptException:
        pass
