#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   display_launch.py
@Time    :   2022/04/08 18:00:42
@Author  :   Cheng Liu 
@Version :   1.0
@Contact :   cliu@umd.edu
@License :   (C)Copyright 2022-2023, Cheng Liu
@Desc    :   This launch file spawns farmbot to Gazebo and Rviz.
'''

import launch
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
import launch_ros
import os

def generate_launch_description():

  pkg_share = launch_ros.substitutions.FindPackageShare(package='farmbot').find('farmbot')
  default_model_path = os.path.join(pkg_share, 'models/Farmbot_v2.urdf')
  rviz_config_path = os.path.join(pkg_share, 'config/urdf_config.rviz')
  robot_des = open(default_model_path).read()
  world_path = os.path.join(pkg_share, 'world/my_world.sdf')
  os.environ["GAZEBO_MODEL_PATH"] = os.path.join(pkg_share, 'models')

  robot_state_publisher_node = launch_ros.actions.Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    parameters=[{'robot_description': robot_des}]
  )
  joint_state_publisher_node = launch_ros.actions.Node(
    package='joint_state_publisher',
    executable='joint_state_publisher',
    name='joint_state_publisher',
    condition=launch.conditions.UnlessCondition(LaunchConfiguration('gui'))
  )
  joint_state_publisher_gui_node = launch_ros.actions.Node(
    package='joint_state_publisher_gui',
    executable='joint_state_publisher_gui',
    name='joint_state_publisher_gui'
  )
  rviz_node = launch_ros.actions.Node(
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    output='screen',
    arguments=['-d', rviz_config_path],
  )
  spawn_entity = launch_ros.actions.Node(
    package='gazebo_ros', 
    executable='spawn_entity.py',
    arguments=['-entity', 'Farmbot_v2', '-topic', 'robot_description'],
    output='screen'
  )


  return launch.LaunchDescription([
    launch.actions.DeclareLaunchArgument(name='gui', default_value='True',
                                        description='Flag to enable joint_state_publisher_gui'),
    launch.actions.ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path], output='screen'),
    joint_state_publisher_node,
    joint_state_publisher_gui_node,
    robot_state_publisher_node,
    spawn_entity,
    rviz_node,

  ])
