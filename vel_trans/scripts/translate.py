#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

joint_pub = None

def joint_callback(data): 
    """twist = Twist()
    twist.linear.x=data.linear.x
    twist.linear.y=data.linear.y
    twist.linear.z=data.linear.z
    twist.angular.x=data.angular.x
    twist.angular.y=data.angular.y
    twist.angular.z=data.angular.z"""
    #data.linear.x*=-1
    if data.angular.z > 0 :
        data.linear.x=(data.angular.z)*(-1) 
        data.angular.z = 0
    elif data.angular.z < 0 :
        data.linear.x=(data.angular.z)*(-1)
        data.angular.z = 0

    elif data.linear.x > 0 :
        data.angular.z=(data.linear.x)
        data.linear.x = 0
    elif data.linear.x < 0 :
        data.angular.z=(data.linear.x)
        data.linear.x = 0
    """x = data.linear.x
    z = data.angular.z 
    data.linear.x= z * (-1)
    data.angular.z = 0
    data.angular.z= x
    data.linear.x = 0"""

    joint_pub.publish(data) # Send it when ready!

if __name__ == '__main__':
    # Init ROS
    rospy.init_node('joint_logger_node', anonymous=True)
    # Subscribers
    rospy.Subscriber('cmd_vel', Twist, joint_callback)
    # Publishers
    joint_pub = rospy.Publisher('test_topic', Twist, queue_size = 10)
    # Spin
    rospy.spin()
