#!/usr/bin/env python
from kinect_controller.srv import tilt, result
import rospy
#criar a class, variavel init -> pub
class Kinect:
    
    def __init__(self, tilt):
        self.pub=Publish(tilt)

    def handle_kinect(tilt):
        #self.pub.Publish(tilt)
        return result("Success")

    def kinect_tilt(self):
        rospy.init_node('kinect_tilt')
        passthrough = rospy.Service('smart_kinect', tilt, handle_kinect)
        self.pub = rospy.Publisher('/kinect/kinect_position_controller/command', float64, queue_size=10)
        rospy.spin()

if __name__ == '__main__':
    Kinect()