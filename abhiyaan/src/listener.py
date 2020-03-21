#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def msgprinter(message):
    print(message.data)


def listener():
    rospy.init_node('MessgListener', anonymous=False)
    rospy.Subscriber('welcome_message', String, callback=msgprinter)
    rospy.spin()
    

if __name__=='__main__':
    listener()