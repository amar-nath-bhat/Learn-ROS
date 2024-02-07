#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Kill
from turtlesim.msg import Pose
from math import atan2, sqrt
from turtlesim_controller.srv import spawn_kill, spawn_killResponse

class BotController:
    def __init__(self):
        rospy.init_node('bot_controller')
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.turtle_pose = Pose() 
        self.kill_proxy = rospy.ServiceProxy('/kill', Kill)
        self.spawn_kill_service = rospy.Service('/spawn_kill', spawn_kill, self.handle_func)
        self.rate = rospy.Rate(1)  # 1 Hz
        self.velocity = Twist()
        self.vel_x = 2
        self.z = 2

    def pose_callback(self, data):
        self.turtle_pose = data
    
    def move(self, linear_speed, angular_speed, duration):
        vel_msg = Twist()
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = angular_speed

        start_time = rospy.Time.now().to_sec()

        while (rospy.Time.now().to_sec() - start_time) < duration:
            self.vel_pub.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.vel_pub.publish(vel_msg)

    def go_to_goal(self, goal_x, goal_y):
        distance = sqrt((goal_x - self.turtle_pose.x)**2 + (goal_y - self.turtle_pose.y)**2)
        rospy.loginfo(distance)
        while distance > 0.1:
            rospy.loginfo("I'm in go 2 goal while loops")

            linear_speed = distance
            angular_speed = (atan2(goal_y - self.turtle_pose.y, goal_x - self.turtle_pose.x) - self.turtle_pose.theta)

            self.move(linear_speed, angular_speed, 0.1)

            distance = sqrt((goal_x - self.turtle_pose.x)**2 + (goal_y - self.turtle_pose.y)**2)

    def kill_bot(self):
        try:
            self.kill_proxy("random_bot")
            rospy.loginfo("Killed the bot")
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: {}".format(e))

    def handle_func(self, req):
        self.go_to_goal(req.x, req.y)
        self.rate.sleep()
        self.kill_bot()
        self.rate.sleep()
        return spawn_killResponse()

if __name__ == '__main__':
    bot_controller = BotController()
    rospy.spin()

