#include "ros/ros.h"
#include "robot_pkg/Message.h"
#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "talkercpp");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<robot_pkg::Message>("chatter", 1000);

  ros::Rate loop_rate(10);
  int count = 0;
  while (ros::ok())
  {
    robot_pkg::Message msg;
    msg.message = "Publisher Working!";
    msg.number1 = 10;
    msg.number2 = 2.9;
    msg.decision = true;
    ROS_INFO("%s", msg.message.c_str());
    chatter_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
    ++count;
  }


  return 0;
}