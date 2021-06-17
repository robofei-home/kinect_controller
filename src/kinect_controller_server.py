#!/usr/bin/env python
from kinect.srv import tilt, result
import rospy

def handle_kinect(tilt):
    return result(tilt)

def kinect_tilt():
    #pub = rospy.Publisher('/kinect/kinect_position_controller/command', float64, queue_size=10)
    rospy.init_node('kinect_tilt')
    passthrough = rospy.Service('smart_kinect', tilt, handle_kinect)
    rospy.spin()

if __name__ == "__main__":
    kinect_tilt_server()