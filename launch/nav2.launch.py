import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    pkg_share = get_package_share_directory('suraqil_bot')
    nav2_bringup_share = get_package_share_directory('nav2_bringup')

    default_map = os.path.join(pkg_share, 'map', 'map.yaml')
    default_params = os.path.join(pkg_share, 'config', 'nav2_params.yaml')
    nav2_launch_file = os.path.join(nav2_bringup_share, 'launch', 'bringup_launch.py')

    map_arg = LaunchConfiguration('map')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map', default_value=default_map,
            description='Full path to map yaml file to load.'
        ),
        DeclareLaunchArgument(
            'use_sim_time', default_value='true',
            description='Use simulation time if true.'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch_file),
            launch_arguments={
                'map': map_arg,
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'autostart': 'true',
                'slam': 'false',
            }.items(),
        ),
    ])
