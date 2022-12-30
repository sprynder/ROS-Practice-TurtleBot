#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

move = Twist()
move.linear.x = 0.5
move.angular.z = 0
rospy.init_node("topics_quiz_node")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
r = rospy.Rate(2)
pub.publish(move)


def callback(mess):
    left = mess.ranges[719]
    right = mess.ranges[0]
    middle = mess.ranges[360]
    if middle < 1 or right < 1:
        move.angular.z = 1
    elif left < 1:
        move.angular.z = -1
    else:
        move.angular.z = 0


sub = rospy.Subscriber("/kobuki/laser/scan", LaserScan, callback)
while not rospy.is_shutdown():
    pub.publish(move)
    r.sleep()
