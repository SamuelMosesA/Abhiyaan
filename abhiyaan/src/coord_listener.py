#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def msgprinter(message):
    print(message.x)


def listener():
    rospy.init_node('MessgListener', anonymous=False)
    rospy.Subscriber('/turtle1/pose', Pose, callback=msgprinter)
    rospy.spin()
    

if __name__=='__main__':
    listener()