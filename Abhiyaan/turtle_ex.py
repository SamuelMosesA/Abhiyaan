#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan, sqrt


class TurtleSim:
    def __init__(self):
        rospy.init_node('turtle_exercise', anonymous=False)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber(
            '/turtle1/pose', Pose, callback=self.coord_return)

        self.command = Twist()
        self.cur = Pose()
        self.rate = rospy.Rate(20)

    def coord_return(self, coord):
        self.cur = coord
        print(self.cur)

    def distance(self):
        d_x = 10-self.cur.x
        d_y = 10-self.cur.y

        return sqrt(d_x**2 + d_y**2)

    def turn_angle(self):
        required_angle = atan((10 - self.cur.y)/(10-self.cur.x))
        turn_angle = required_angle - self.cur.theta

        return turn_angle

    def controller(self):
        while (self.distance()-2 > 10**-1):
            self.command.linear.x = self.distance()
            self.command.angular.z = 3*self.turn_angle()
            self.pub.publish(self.command)
            self.rate.sleep()
        
        self.command.linear.x = 0
        self.command.angular.z = 0
        self.pub.publish(self.command)

        rospy.spin()

if __name__ == '__main__':
    turtle1 = TurtleSim()
    try:
        turtle1.controller()
    except rospy.ROSInterruptException:
        pass
