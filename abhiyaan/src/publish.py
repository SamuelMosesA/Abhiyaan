#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def publisher():
    publ = rospy.Publisher('welcome_message', String, queue_size=15)
    rospy.init_node('MessgPublisher', anonymous=False)
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        welcomeStr = "Welcome to Abhiyaan"
        publ.publish(welcomeStr)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
