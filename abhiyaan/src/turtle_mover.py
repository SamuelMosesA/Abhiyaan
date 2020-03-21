#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan,sqrt


rospy.init_node('turtle_exercise', anonymous=False)
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
coordinate = Pose()
rate = rospy.Rate(10)

def coord_return(coord):
    coordinate = coord
    
    

def lin_mover(d):
    command = Twist()
    command.linear.x = d
    pub.publish(command)
    
def to_turn():

    required_angle = atan((10 - coordinate.y)/(10-coordinate.x))
    turn_angle = required_angle - coordinate.theta

    return turn_angle


def distance(coord):
    dist_x = 10-coord.x
    dist_y = 10-coord.y

    return sqrt(dist_x**2 + dist_y**2)



def controller():
    rospy.Subscriber('/turtle1/pose', Pose, callback=coord_return)
    rotate = Twist()
    rotate.angular.z = 5.0
    
    while not rospy.is_shutdown():
        
        if(to_turn()>10**-4):
            print(coordinate)
            pub.publish(rotate)  

        if(distance(coordinate)-2>10**-4):    
            print(coordinate)
            lin_mover(2.0) 
        rate.sleep() 

    
    rospy.spin()
    

    


if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass
