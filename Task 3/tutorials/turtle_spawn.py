#!/usr/bin/env python3

import rospy
import random
from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from turtlesim_controller.srv import spawn_kill, spawn_killResponse

class SpawnKillRobot():
    def __init__(self):
        self.random_bot_pose_sub = rospy.Subscriber('/random_bot/pose', Pose, self.pose_callback)
        self.random_bot_pose = Pose()

    def pose_callback(self, data):
        self.random_bot_pose = data   

    def spawn_random_bot(self):
        rospy.wait_for_service('/spawn')
        try:
            spawn_proxy = rospy.ServiceProxy('/spawn', Spawn)
            x = random.uniform(1, 10)
            y = random.uniform(1, 10)
            spawn_proxy(x, y, 0, "random_bot")
            rospy.loginfo("Spawned bot at ({}, {})".format(x, y))
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: {}".format(e))

    def kill_random_bot(self):
        try:
            rospy.wait_for_service('spawn_kill')
            spawn_kill_proxy = rospy.ServiceProxy('spawn_kill', spawn_kill)
            resp = spawn_kill_proxy(self.random_bot_pose.x, self.random_bot_pose.y)
            return spawn_killResponse("Bot Killed")
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: {}".format(e))


if __name__ == '__main__':
    rospy.init_node('random_bot_spawner')
    rate = rospy.Rate(1)  
    bot = SpawnKillRobot()
    # while not rospy.is_shutdown():
    bot.spawn_random_bot()
    bot.kill_random_bot()
    rate.sleep()
