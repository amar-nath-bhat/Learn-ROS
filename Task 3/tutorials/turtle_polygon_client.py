#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from turtlesim_controller.srv import polygon, polygonResponse

def draw_polygon_client(n):
    rospy.wait_for_service('draw_polygon')
    try:
        draw_polygon = rospy.ServiceProxy('draw_polygon', polygon)
        resp1 = draw_polygon(n)
        return polygonResponse("Polygon Drawn")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    n = int(sys.argv[1])
    print("Requesting n:%f"%(n))
    print(draw_polygon_client(n))