#!/usr/bin/env python

import sys
import rospy
from kinect_controller.srv import *

#criar a class

def kinect_controller_client(tilt):
    rospy.wait_for_service('smart_kinect')
    try:
        smart_kinect = rospy.ServiceProxy('kinect_tilt', tilt)
        k_info = smart_kinect(tilt)
        return k_info
    except:
        pass

#o client vai pra task

# def usage():
#     return "%s [x y]"%sys.argv[0]

if __name__ == '__main__':
    try:
        teste = kinect_controller_client(0.9)
        print("deu bom? %s", teste)
    except KeyboardInterrupt:
        pass
    # if len(sys.argv) == 3:
    #     x = int(sys.argv[1])
    #     y = int(sys.argv[2])
    # else:
    #     print(usage())
    #     sys.exit(1)
    # print("Requesting %s+%s"%(x, y))
    # print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))