#!/usr/bin/env python
from kinect.srv import tilt, result
import rospy

class Kinect:
    
    def __init__(self, tilt):
        self.pub=Publish(tilt)

    def handle_kinect(tilt):
        return result("Success")

    def kinect_tilt(self):
        rospy.init_node('kinect_tilt')
        passthrough = rospy.Service('smart_kinect', tilt, handle_kinect)
        self.pub = rospy.Publisher('/kinect/kinect_position_controller/command', float64, queue_size=10)
        rospy.spin()

if __name__ == "__main__":
    Kinect()