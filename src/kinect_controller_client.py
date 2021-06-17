#!/usr/bin/env python

import sys
import rospy
from kinect.srv import *

def kinect_controller_client(t):
    rospy.wait_for_service('smart_kinect')
    try:
        smart_kinect = rospy.ServiceProxy('kinect_tilt', tilt)
        k_info = smart_kinect(t)
        return k_info

# def usage():
#     return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    kinect_controller_client()
    # if len(sys.argv) == 3:
    #     x = int(sys.argv[1])
    #     y = int(sys.argv[2])
    # else:
    #     print(usage())
    #     sys.exit(1)
    # print("Requesting %s+%s"%(x, y))
    # print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))