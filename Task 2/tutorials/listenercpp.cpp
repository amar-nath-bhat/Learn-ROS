#include "ros/ros.h"
#include "robot_pkg/Message.h"

void chatterCallback(const robot_pkg::Message::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->message.c_str());
  ROS_INFO("I heard: [%d]", msg->number1);
  ROS_INFO("I heard: [%f]", msg->number2);
  ROS_INFO("I heard: [%d]", msg->decision);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listenercpp");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
  ros::spin();

  return 0;
}