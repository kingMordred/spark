#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

joint_pub = None

def joint_callback(data): 

    #joint_pub.publish(data) # Send it when ready!
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    if data.data=="forward":
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 1
        joint_pub.publish(vel_msg)

    elif data.data=="backward":
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = -1
        joint_pub.publish(vel_msg)

    elif data.data=="turn left":
        vel_msg.linear.x = -1
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        joint_pub.publish(vel_msg)

    elif data.data=="turn right":
        vel_msg.linear.x = 1
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        joint_pub.publish(vel_msg)

    elif data.data=="stop":
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        joint_pub.publish(vel_msg)

    else :
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        joint_pub.publish(vel_msg)
    

if __name__ == '__main__':
    # Init ROS
    rospy.init_node('vcnode', anonymous=True)
    # Subscribers
    rospy.Subscriber('chatter', String, joint_callback)
    # Publishers
    joint_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size = 10)


    # Spin
    rospy.spin()