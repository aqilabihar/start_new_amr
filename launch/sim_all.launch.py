import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory('suraqil_bot')
    
    default_map = os.path.join(pkg_share, 'map', 'map.yaml')

    map_yaml = LaunchConfiguration('map')
    enable_slam = LaunchConfiguration('enable_slam')
    enable_nav2 = LaunchConfiguration('enable_nav2')
    enable_rviz = LaunchConfiguration('enable_rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map', default_value=default_map,
            description='Full path to map yaml file for Nav2 localization.'
        ),
        DeclareLaunchArgument(
            'enable_slam', default_value='true',
            description='Enable SLAM Toolbox for mapping (true or false).'
        ),
        DeclareLaunchArgument(
            'enable_nav2', default_value='false',
            description='Enable Nav2 for autonomous navigation (true or false).'
        ),
        DeclareLaunchArgument(
            'enable_rviz', default_value='true',
            description='Enable RViz visualization (true or false).'
        ),
        
        # 1. Launch Gazebo simulation + robot state publisher + bridge (always)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_share, 'launch', 'launch_sim.launch.py')
            ),
        ),

        # 2. Conditionally launch SLAM Toolbox
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_share, 'launch', 'slam.launch.py')
            ),
            condition=IfCondition(enable_slam),
        ),

        # 3. Conditionally launch Nav2 (only if enable_nav2 is 'true')
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_share, 'launch', 'nav2.launch.py')
            ),
            launch_arguments={
                'map': map_yaml,
                'use_sim_time': 'true',
            }.items(),
            condition=IfCondition(enable_nav2),
        ),

        # 4. Conditionally launch RViz
        Node(
            condition=IfCondition(enable_rviz),
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
        ),
    ])
