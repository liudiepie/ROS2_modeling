#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   move.py
@Time    :   2022/04/08 17:53:29
@Author  :   Cheng Liu 
@Version :   1.0
@Contact :   cliu@umd.edu
@License :   (C)Copyright 2022-2023, Cheng Liu
@Desc    :   None
'''

import rclpy
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from rclpy.node import Node

x = 0.0
y = 0.0 
theta = 0.0

class move_node(Node):
    def __init__(self):
        """_summary_
        This class subscribe odom to get the pose and publish the Twist to cmd_vel
        The publish rate is 30hz
        """
        super().__init__("movePub")
        self.move_publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.move_timer = self.create_timer(1/30, self.publish_move)
        self.move_subscriber = self.create_subscription(Odometry, "/odom", self.newOdom,10)
        self.move_subscriber

    def newOdom(self, msg):
        """_summary_

        Args:
            msg (_type_ Point): _description_
            callback function for subscriber, this callback is to get the x, y, and angle of farmbot
            To find the theta, we need to transform euler to quaternion
        """
        global x
        global y
        global theta

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        rot_q = msg.pose.pose.orientation
        (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
        
    def publish_move(self):
        """_summary_
        This function makes farmbot to go to certain position
        The way it moves is simple. When theta is > 0.1, farmbot will turn.
        When theta is < 0.1, farm will go forward.
        """
        global x
        global y
        global theta
        speed = Twist()
        goal = Point()
        goal.x = -3.0
        goal.y = -3.0
    	
        inc_x = goal.x -x
        inc_y = goal.y -y
        angle_to_goal = atan2(inc_y, inc_x)
        if abs(angle_to_goal - theta) > 0.1:
            speed.linear.x = 0.0
            speed.angular.z = 0.3
            self.move_publisher.publish(speed)
        else:
            speed.linear.x = 0.5
            speed.angular.z = 0.0
            self.move_publisher.publish(speed)

def main(args=None):

    rclpy.init(args=args)
    node = move_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
